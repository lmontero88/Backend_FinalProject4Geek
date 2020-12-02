from flask import request
from flask_restx import Resource

from ..utils.decorator import admin_token_required
from ..utils.dto import UserDto
from ..services.user_service import save_new_user, get_all_users

api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('Retorna la lista de usuarios registrados')
    @admin_token_required
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """Lista todos los usuarios registrados"""
        return get_all_users()

    @api.expect(_user, validate=True)
    @api.response(201, 'Usuario registrado correctamente.')
    @api.doc('create a new user')
    def post(self):
        """Registra un nuevo usuario"""
        data = request.json
        return save_new_user(data=data)


