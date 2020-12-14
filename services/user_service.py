import uuid
import datetime

from flask import jsonify, request

from manage import db
from model.user import User


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    role_id = 1  # lo ponemos como jugador
    if data.get('isTeacher', False):
        role_id = 2
    if not user:
        new_user = User(
            email=data['email'],
            first_name=data['firstName'],
            last_name=data['lastName'],
            password=data['password'],
            role_id=role_id,
            birthdate=datetime.datetime.strptime(data['birthdate'], '%Y-%m-%d'),
            gender=data['gender'],
            registered_at=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        auth_token = new_user.encode_auth_token()
        if auth_token:
            response_object = {
                'status': 'success',
                'message': 'Usuario registrado correctamente.',
                'Authorization': auth_token.decode()
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


# Modificar perfil
def edit_profile():
    user_email = request.json.get("user_email", None)
    if not user_email:
        return jsonify({"msg": "Email no puede estar vacio"}), 400
    user_found = User.query.filter_by(email=user_email).first()
    if not user_found:
        return jsonify({"msg": "Email no válido"}), 400
    status = request.json.get("status")
    phones = request.json.get("phones")
    photo = request.json.get("photo")
    bio = request.json.get("bio")
    if not status or not phones or not photo:
        return jsonify({"msg": "Los campos estado, foto y telefono no pueden estar vacios"}), 400
    user_found.status = status
    user_found.phones = phones
    user_found.photo = photo
    user_found.bio = bio
    user_found.save_changes()
    return jsonify({"msg": "Cambios guardados correctamente"}), 200

# Registro usuario
# def registro_datos_user():
#     if request.method == 'POST':
#         email = request.json.get('email')
#         if not email:
#             return jsonify({"msg":"Email es requerido"}), 400
#         first_name = request.json.get("first_name")
#         last_name = request.json.get("last_name")
#         birthdate = request.json.get("birthdate")
#         phones = request.json.get ("phones")
#         gender = request.json.get("gender")
#         status = request.json.get("status")
#         photo = request.json.get("photo")
#         role_id = request.json.get("isTeacher", 1)
#         if not first_name or not last_name or not birthdate or not phones or not gender or not status or not photo:
#             return jsonify({"msg":"Datos incompletos"}), 400
#
#         user = User.query.filter_by(email=email).first()
#         if user:
#             return jsonify({"msg": "Usuario ya registrado"}), 400
#         user = User()
#         user.last_name = last_name
#         user.birthdate = birthdate
#         user.phones = phones
#         user.gender = gender
#         user.role_id = role_id
#         #user.status = status
#         #user.photo = photo
#         user.save_changes()
#         return jsonify({"msg":"Usuario registrado correctamente"}), 200
