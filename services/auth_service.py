from model.user import User


def login_user(data):
    user = User.query.filter_by(email=data.get('email')).first()
    if user and user.check_password(data.get('password')):
        auth_token = user.encode_auth_token()
        if auth_token:
            response_object = {
                'status': 'success',
                'message': 'Usuario logueado correctamente.',
                'Authorization': auth_token.decode()
            }
            return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Usuario o contraseña incorrecta.'
        }
        return response_object, 401


def get_logged_in_user(new_request):
    # get the auth token
    auth_token = new_request.headers.get('Authorization')
    if auth_token:
        resp = User.decode_auth_token(auth_token)
        if not isinstance(resp, str):
            user = User.query.filter_by(id=resp).first()
            response_object = {
                'status': 'success',
                'data': {
                    'user_id': user.id,
                    'email': user.email,
                    'role_id': user.role_id,
                    'registered_at': str(user.registered_at)
                }
            }
            return response_object, 200
        response_object = {
            'status': 'fail',
            'message': resp
        }
        return response_object, 401
    else:
        response_object = {
            'status': 'fail',
            'message': 'Por favor, proporcione un token correcto.'
        }
        return response_object, 401
