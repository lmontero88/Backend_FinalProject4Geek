from flask_restx import Api
from flask import Blueprint

from .v1.controller.auth_controller import api as auth_ns
from .v1.controller.user_controller import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='API 4Geeks Final Project',
          version='1.0',
          description='API para el pryecto final de 4Geeks'
          )

api.add_namespace(auth_ns, path='/api/v1/auth')
api.add_namespace(user_ns, path='/api/v1/users')
