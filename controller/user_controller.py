from flask import request

from app import app
from utils.decorator import admin_token_required, token_required
from services.user_service import save_new_user, get_all_users


@app.route("/api/users", methods=['POST'])
def create_user():
    try:
        data = request.json
        if not data.get('email', None) or not data.get('firstName', None) or not data.get('lastName', None) or not data.get('password', None):
            return {
                       'status': 'fail',
                       'message': "Solicitud incorrecta. Faltan campos requeridos."
                   }, 400
        response = save_new_user(data)
    except Exception as e:
        return {
            'status': 'fail',
            'message': e.__str__(),
        }, 500
    return response


@admin_token_required
@app.route("/api/users", methods=['GET'])
def get_users():
    """Lista todos los usuarios registrados"""
    return get_all_users()

