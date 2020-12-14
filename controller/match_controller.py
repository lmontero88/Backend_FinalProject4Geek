from flask import request
from app import app
from services.match_services import get_all_jugadores, create_match_players, get_my_pending_matchs, get_my_friends, update_match,get_jugadores
from utils.decorator import token_required


@app.route("/api/players", methods=['GET'])
@token_required
def jugadores_disponibles(data_token):
    return get_all_jugadores(data_token)


@app.route("/api/players/<id>", methods=['GET'])
@token_required
def jugador_disponible(data_token, id):
    return get_jugadores(id)


@app.route("/api/matchs", methods=['POST'])
@token_required
def create_match():
    try:
        user_id_from = request.json.get('user_id_from', None)
        user_id_to = request.json.get('user_id_to', None)

        if not user_id_to or not user_id_from:
            return {
                       'status': 'fail',
                       'message': "Solicitud incorrecta. Faltan campos requeridos."
                   }, 400
        response = create_match_players(user_id_from, user_id_to)
    except Exception as e:
        return {
            'status': 'fail',
            'message': e.__str__(),
        }, 500
    return response


@app.route("/api/matchs/pending/<user_id>", methods=['GET'])
@token_required
def get_pending_matchs(user_id):
    try:
        return get_my_pending_matchs(user_id)
    except Exception as e:
        return {
            'status': 'fail',
            'message': e.__str__(),
        }, 500


@token_required
@app.route("/api/matchs/<user_id>", methods=['GET'])
def get_my_matchs(user_id):
    try:
        return get_my_friends(user_id)
    except Exception as e:
        return {
            'status': 'fail',
            'message': e.__str__(),
        }, 500


@app.route("/api/matchs", methods=['PUT'])
@token_required
def update_request_match():
    try:
        match_id = request.json.get('match_id', None)
        is_accepted = request.json.get('is_accepted', False)

        if not match_id:
            return {
                       'status': 'fail',
                       'message': "Solicitud incorrecta. Faltan campos requeridos."
                   }, 400
        return update_match(match_id, is_accepted)
    except Exception as e:
        return {
            'status': 'fail',
            'message': e.__str__(),
        }, 500

    return
