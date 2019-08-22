import os
from flask import Flask
from flask_restplus import Api

from prometheus_flask_exporter import PrometheusMetrics

metrics = PrometheusMetrics(app=None)

VERSION = os.environ.get('VERSION_NAME', 'BAD VERSION')


def create_app(script=False):
    from users_backend.api_namespace import api_namespace
    from users_backend.admin_namespace import admin_namespace

    application = Flask(__name__)

    if not script:
        # Initialise metrics
        metrics.init_app(application)

    api = Api(application, version=VERSION, title='Users Backend API',
              description='A Simple CRUD API')

    from users_backend.db import db, db_config
    application.config['RESTPLUS_MASK_SWAGGER'] = False
    application.config.update(db_config)
    db.init_app(application)
    application.db = db

    api.add_namespace(api_namespace)
    api.add_namespace(admin_namespace)

    return application
