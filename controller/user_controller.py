from flask import request

from app import app
from ..utils.decorator import admin_token_required, token_required
from ..services.user_service import save_new_user, get_all_users


@app.route("api/users", methods=['POST'])
def create_user():
    data = request.json
    return save_new_user(data=data)


@admin_token_required
@app.route("api/users", methods=['GET'])
def get_users():
    """Lista todos los usuarios registrados"""
    return get_all_users()