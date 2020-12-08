import uuid
import datetime

from manage import db
from model.user import User


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    role_id = 1  # lo ponemos como jugador
    if data['isTeacher']:
        role_id = 2
    if not user:
        new_user = User(
            email=data['email'],
            first_name=data['firstName'],
            last_name=data['lastName'],
            password=data['password'],
            role_id=role_id,
            registered_at=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Usuario registrado correctamente.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Usuario ya existe.',
        }
        return response_object, 409


def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
