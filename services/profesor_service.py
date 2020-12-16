from model.user import User
from flask import jsonify


def get_all_profesores(data_token):
    profesores = User.query.filter_by(role_id=2, status=True).all()
    json_profesores = list(map(lambda l:  {
            "id": l.id,
            "firstname": l.first_name,
            "lastname": l.last_name,
            "photo": l.photo,
        }, list(filter(lambda j: (j.id != data_token.get('user_id')), profesores))))
    return jsonify(json_profesores)


def get_profesor(id):
    if id is not None:
        profesor = User.query.get(id)
        if profesor:
            return jsonify(profesor.serialize()), 200
        else:
            return jsonify({"msg": "Profesor doesn't exist"}), 404
    else:
        profesores = User.query.all()
        profesores = list(map(lambda contact: contact.serialize(), profesores))
        return jsonify(profesores), 200