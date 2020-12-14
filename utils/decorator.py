from functools import wraps

from flask import request

from services.auth_service import get_logged_in_user


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not 'Authorization' in request.headers:
            response_object = {
                'status': 'fail',
                'message': 'Token requerido'
            }
            return response_object, 401

        data, status = get_logged_in_user(request)
        data_token = data.get('data')

        if not data_token:
            return data_token, status

        return f(data_token, *args, **kwargs)

    return decorated


def admin_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status

        admin = token.get('admin')
        if not admin:
            response_object = {
                'status': 'fail',
                'message': 'Token de administrador requerido'
            }
            return response_object, 401

        return f(*args, **kwargs)

    return decorated
