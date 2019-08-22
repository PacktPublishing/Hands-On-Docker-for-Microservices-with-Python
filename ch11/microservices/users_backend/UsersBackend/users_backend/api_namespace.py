import http.client
from flask_restplus import Namespace, Resource, fields
from users_backend import config
from users_backend.models import UserModel
from users_backend.token_validation import validate_token_header
from users_backend.token_validation import generate_token_header
from users_backend.db import db
from flask import abort

api_namespace = Namespace('api', description='API operations')


def authentication_header_parser(value):
    username = validate_token_header(value, config.PUBLIC_KEY)
    if username is None:
        abort(401)
    return username


# Input and output formats for Users

authentication_parser = api_namespace.parser()
authentication_parser.add_argument('Authorization', location='headers',
                                   type=str,
                                   help='Bearer Access Token')

login_parser = api_namespace.parser()
login_parser.add_argument('username', type=str, required=True,
                          help='username')
login_parser.add_argument('password', type=str, required=True,
                          help='password')


@api_namespace.route('/login/')
class UserLogin(Resource):

    @api_namespace.doc('login')
    @api_namespace.expect(login_parser)
    def post(self):
        '''
        Login and return a valid Authorization header
        '''
        args = login_parser.parse_args()

        # Search for the user
        user = (UserModel
                .query
                .filter(UserModel.username == args['username'])
                .first())
        if not user:
            return '', http.client.UNAUTHORIZED

        # Check the password
        # REMEMBER, THIS IS NOT SAFE. DO NOT STORE PASSWORDS IN PLAIN
        if user.password != args['password']:
            return '', http.client.UNAUTHORIZED

        # Generate the header
        header = generate_token_header(user.username, config.PRIVATE_KEY)
        return {'Authorized': header}, http.client.OK
