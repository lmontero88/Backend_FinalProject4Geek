import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask.templating import render_template
from api import blueprint
from api.v1.app import create_app, db
from api.v1.model import user, user_sport,sport,clasificado,favourite_product,favourite_user,profile,match,role

# no quitar, es para que migre


from dotenv import load_dotenv
load_dotenv()

app = create_app(os.getenv('ENVIRONMENT') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()

@app.route('/')
def root():
    return render_template('index.html')

if __name__ == '__main__':
    manager.run()
