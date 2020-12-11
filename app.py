import os
from flask import Flask
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))
flask_bcrypt = Bcrypt()

app = Flask(__name__)
CORS(app)  # esto no deberia quedarse asi, pues es global
app.url_map.strict_slashes = False

key = os.getenv('SECRET_KEY', 'my_precious_secret_key')
app.config['SECRET_KEY'] = key
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

flask_bcrypt.init_app(app)

jwt = JWTManager(app)
# no quitar esto, sino no ve las rutas y siempre dara 404
# por cada controller que se cree se debe agregar su import aqui
from controller.auth_controller import *
from controller.user_controller import *
from controller.match_controller import *
from controller.recuperar_pass_controller import *


if __name__ == '__main__':
    app.run()
