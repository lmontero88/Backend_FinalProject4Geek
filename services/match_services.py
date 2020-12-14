from model.user import User
from model.match import Match
from model.friend import Friend
from flask import jsonify
from sqlalchemy import or_, and_
from manage import db


def get_all_jugadores(data_token):
    jugadores = User.query.filter_by(role_id=1, status=True).all()
    json_jugadores = list(map(lambda l:  {
            "id": l.id,
            "firstname": l.first_name,
            "lastname": l.last_name,
            "photo": l.photo,
        }, list(filter(lambda j: (j.id != data_token.get('user_id')), jugadores))))
    return jsonify(json_jugadores)


def get_jugadores(id):
    if id is not None:
        jugador = User.query.get(id)
        if jugador:
            return jsonify(jugador.serialize()), 200
        else:
            return jsonify({"msg": "Jugador doesn't exist"}), 404
    else:
        jugadores = User.query.all()
        jugadores = list(map(lambda contact: contact.serialize(), jugadores))
        return jsonify(jugadores), 200


def create_match_players(user_id_from, user_id_to):
    user_from = User.query.get(user_id_from)
    user_to = User.query.get(user_id_to)

    if not user_from or not user_to:
        response_object = {
            'status': 'fail',
            'message': 'Usuario no encontrado'
        }
        return response_object, 404

    match = Match(user_from_id=user_id_from, user_to_id=user_id_to)

    save_changes(match)
    response_object = {
        'status': 'success',
        'message': 'Match enviado correctamente.'
    }
    return response_object, 200


def get_my_pending_matchs(user_id):
    # solicitudes de amistad que le han enviado
    pending_matchs = Match.query.filter(and_(Match.user_to_id==user_id, Match.status_request==0)).all()

    pending_user_ids = []
    for match in pending_matchs:
        pending_user_ids.append(match.user_from_id)

    if len(pending_user_ids) == 0:
        return jsonify([])

    pending_users = User.query.filter(User.id.contains(pending_user_ids)).all()
    json_pending_users = list(map(lambda l: l.serialize(), pending_users))
    return jsonify(json_pending_users)


def get_my_friends(user_id):
    # Dame las amistades en las cuales el usuario esta presente
    friends = Friend.query.filter_by(user_id=user_id).all()

    # Dame el id de sus amigos
    user_ids = []
    for friend in friends:
        user_ids.append(friend.friend_id)

    if len(user_ids) == 0:
        return jsonify([])

    friends_of_user = User.query.filter(User.id.contains(user_ids)).all()
    json_friends_of_user = list(map(lambda l: l.serialize(), friends_of_user))
    return jsonify(json_friends_of_user)


def update_match(match_id, is_accepted):
    match = Match.query.get(match_id)

    if not match:
        response_object = {
            'status': 'fail',
            'message': 'Match no encontrado'
        }
        return response_object, 404

    match.status_request = 1 if is_accepted else -1

    update()

    if is_accepted:
        friend1 = Friend(user_id=match.user_from_id, friend_id=match.user_to_id)
        friend2 = Friend(user_id=match.user_to_id, friend_id=match.user_from_id)

        save_changes(friend1)
        save_changes(friend2)

    response_object = {
        'status': 'success',
        'message': 'Solicitud actualizada correctamente'
    }
    return response_object, 200


def update():
    db.session.commit()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
