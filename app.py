import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
flask_bcrypt = Bcrypt()

app = Flask(__name__)
CORS(app)  # esto no deberia quedarse asi, pues es global
app.url_map.strict_slashes = False

key = os.getenv('SECRET_KEY', 'my_precious_secret_key')
app.config['SECRET_KEY'] = key
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
flask_bcrypt.init_app(app)

migrate = Migrate(app, db)

manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':#esto es para iniciar servidor Flask
    manager.run()