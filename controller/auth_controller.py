from flask import request

from app import app

from services.auth_service import login_user


@app.route("/api/auth/login", methods=['POST'])
def user_login():
    try:
        data = request.json
        if not data.get('email', None) or not data.get('password', None):
            return {
                   'status': 'fail',
                   'message': "Solicitud incorrecta. Faltan campos requeridos."
               }, 400
        return login_user(data)
    except Exception as e:
        return {
                   'status': 'fail',
                   'message': e.__str__(),
               }, 500
