import logging
from flask import Flask, request, has_request_context
from flask import current_app, g

from flask_restplus import Api
from flask_request_id_header.middleware import RequestID
from logging.config import dictConfig
from time import time

from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Histogram, Counter

metrics = PrometheusMetrics(app=None)

METRIC_REQUESTS = Counter('requests', 'Requests',
                                  ['endpoint', 'method', 'status_code'])
METRIC_REQ_TIME = Histogram('req_time', 'Req time in ms',
                            ['endpoint', 'method', 'status_code'])


class RequestFormatter(logging.Formatter):
    ''' Inject the HTTP_X_REQUEST_ID to format logs '''

    def format(self, record):
        record.request_id = 'NA'

        if has_request_context():
            record.request_id = request.environ.get("HTTP_X_REQUEST_ID")

        return super().format(record)


dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


def logging_before():
    msg = 'REQUEST {REQUEST_METHOD} {REQUEST_URI}'.format(**request.environ)
    current_app.logger.info(msg)

    # Store the start time for the request
    g.start_time = time()


def logging_after(response):
    # Get total time in milliseconds
    total_time = time() - g.start_time
    time_in_ms = int(total_time * 1000)
    msg = f'RESPONSE TIME {time_in_ms} ms'
    current_app.logger.info(msg)

    msg = f'RESPONSE STATUS {response.status_code}'
    current_app.logger.info(msg)

    # Store metrics
    endpoint = request.endpoint
    method = request.method.lower()
    status_code = response.status_code
    METRIC_REQUESTS.labels(endpoint, method, status_code).inc()
    METRIC_REQ_TIME.labels(endpoint, method, status_code).observe(time_in_ms)

    return response


def create_app(script=False):
    from thoughts_backend.api_namespace import api_namespace
    from thoughts_backend.admin_namespace import admin_namespace

    application = Flask(__name__)
    application.before_request(logging_before)
    application.after_request(logging_after)

    # Enable RequestId
    application.config['REQUEST_ID_UNIQUE_VALUE_PREFIX'] = ''
    RequestID(application)

    if not script:
        # For scripts, it should not connect to Syslog
        handler = logging.handlers.SysLogHandler(('syslog', 5140))
        req_format = ('[%(asctime)s] %(levelname)s [%(request_id)s] '
                      '%(module)s: %(message)s')
        handler.setFormatter(RequestFormatter(req_format))
        handler.setLevel(logging.INFO)
        application.logger.addHandler(handler)
        # Do not propagate to avoid log duplication
        application.logger.propagate = False

        # Initialise metrics
        metrics.init_app(application)

    api = Api(application, version='0.1', title='Thoughts Backend API',
              description='A Simple CRUD API')

    from thoughts_backend.db import db, db_config
    application.config['RESTPLUS_MASK_SWAGGER'] = False
    application.config.update(db_config)
    db.init_app(application)
    application.db = db

    api.add_namespace(api_namespace)
    api.add_namespace(admin_namespace)

    return application
