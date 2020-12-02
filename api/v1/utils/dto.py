from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='Endpoints relacionadas con el usuario.')
    user = api.model('user', {
        'email': fields.String(required=True, description='Correo electrónico'),
        'username': fields.String(required=True, description='Nombre de usuario'),
        'password': fields.String(required=True, description='Contraseña'),
    })


class AuthDto:
    api = Namespace('auth', description='Endpoints relacionados a autenticación.')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='Correo electrónico'),
        'password': fields.String(required=True, description='Contraseña'),
    })