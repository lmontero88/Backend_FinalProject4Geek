#Recuperar contraseña
from flask import request
from app import app
from services.recuperar_pass_service import resetearPassword, recuperacion


@app.route("/api/recuperar-password", methods=['POST'])
def recuperar_pass():
    """Permite que el usuario recupere la contraseña"""
    return recuperacion()


#Reset Password
@app.route("/api/reset-password", methods=['POST'])
def reset_pass():
    return resetearPassword()