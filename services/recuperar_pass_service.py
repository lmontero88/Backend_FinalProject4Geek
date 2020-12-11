import os
import datetime
import time

from flask_bcrypt import generate_password_hash
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
from flask import jsonify, request
from sendgrid import SendGridAPIClient, sendgrid
from sendgrid.helpers.mail import Mail

from model.user import User

# Recuperar contraseña

def recuperacion():
    email = request.json.get("email")
    if not email:
        return jsonify({"msg": "El email es requerido"}), 400
    else:
        user_email_found = User.query.filter_by(email=email).first()
        if not user_email_found:
            return jsonify({"msg": f"El email no se encuentra registrado"}), 404
        else:
            expire_in = datetime.timedelta(hours=1)
            access_token = create_access_token(identity=user_email_found.email, expires_delta=expire_in)
            url = f"http://localhost:3000/recuperar-password/{access_token}"
            mensaje = Mail(
                from_email="ojedamartinasofia@gmail.com",
                to_emails = email,
                subject = "Email Recuperacion de Contraseña",
                html_content= f"<html><head></head><body>Para recuperar tu contraseña, usa el siguiente <a href=\"{url}\">Link</a></body></html>"
            )
            try:
                sg = SendGridAPIClient('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')
                response = sg.send(message=mensaje)
                print(response.status_code)
                print(response.body)
                print(response.headers)
                return jsonify({"msg": "Se ha enviado un email a {email} para recuperar la contraseña"}), 200
            except Exception as e:
                print(e)

            # url = f"http://localhost:3000/recuperar-password/{access_token}"
            # mensaje = f"<html><head></head><body>Para recuperar tu contraseña, usa el siguiente <a href=\"{url}\">Link</a></body></html>"
            # content = Content("text/html", mensaje)
            # response = sg.send(mensaje)
            # print(response.status_code)
            # print(response.body)
            # print(response.headers)
            # return jsonify({"msg": "Se ha enviado un email a {email} para recuperar la contraseña"}), 200


# Resetear Pass
def resetearPassword():
    @jwt_required
    def resetearPassword():
        contraseña = request.json.get("password")

        id = get_jwt_identity()
        user = User.query.get(id)
        if user:
            user.password = generate_password_hash(contraseña)
            user.save()
            expire_in = datetime.timedelta(days=1)
            data = {
                "access_token": create_access_token(identity=user.email, expires_delta=expire_in),
                "user": user.serialize()
            }
            return jsonify({"msg": "contraseña cambiada exitosamente"}), 200
        if not user:
            return jsonify({"msg": "usuario no encontrado"}), 404