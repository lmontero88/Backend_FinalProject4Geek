from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app

db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from model.clasificado import *
from model.favourite_product import *
from model.favourite_user import *
from model.match import *
from model.role import *
from model.sport import *
from model.user import *
from model.user_sport import *

if __name__ == '__main__':
    manager.run()