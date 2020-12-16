from flask import request
from app import app
from services.profesor_service import get_all_profesores, get_profesor
from utils.decorator import token_required


@app.route("/api/profesores", methods=['GET'])
@token_required
def profesor_disponibles(data_token):
    return get_all_profesores(data_token)


@app.route("/api/profesor/<id>", methods=['GET'])
@token_required
def profesor_disponible(data_token, id):
    return get_profesor(id)
