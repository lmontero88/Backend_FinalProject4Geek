from flask import request
from flask_restx import Resource

from ..services.auth_service import Auth
from ..utils.dto import AuthDto

api = AuthDto.api
user_auth = AuthDto.user_auth


@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        """
            Autentica un usuario
        """
        post_data = request.json
        return Auth.login_user(data=post_data)
