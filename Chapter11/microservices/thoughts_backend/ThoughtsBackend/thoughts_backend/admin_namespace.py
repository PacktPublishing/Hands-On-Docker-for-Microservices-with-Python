import os
import http.client
from flask_restplus import Namespace, Resource
from thoughts_backend.models import ThoughtModel
from thoughts_backend.db import db

admin_namespace = Namespace('admin', description='Admin operations')


@admin_namespace.route('/thoughts/<int:thought_id>/')
class ThoughtsDelete(Resource):

    @admin_namespace.doc('delete_thought',
                         responses={http.client.NO_CONTENT: 'No content'})
    def delete(self, thought_id):
        '''
        Delete a thought
        '''
        thought = ThoughtModel.query.get(thought_id)
        if not thought:
            # The thought is not present
            return '', http.client.NO_CONTENT

        db.session.delete(thought)
        db.session.commit()

        return '', http.client.NO_CONTENT


@admin_namespace.route('/version/')
class Version(Resource):

    @admin_namespace.doc('get_version')
    def get(self):
        '''
        Return the version of the application
        '''
        data = {
            'commit': os.environ['VERSION_SHA'],
            'version': os.environ['VERSION_NAME'],
        }

        return data
