from flask import request

from app import app


from ..services.auth_service import Auth


@app.route("/api/auth/login", methods=['POST'])
def user_login():
    post_data = request.json
    return Auth.login_user(data=post_data)