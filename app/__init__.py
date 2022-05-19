from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'tours.db'


def create_app(config_name):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'tours'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # Initialise our db
    db.init_app(app)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # importing our blueprints
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint

    # Registering our blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/')

    # import our db object classes
    from .models import User, Booking, Comment

    create_database(app)

    return app


# create our db
def create_database(app):
    if not path.exists('app/' + DB_NAME):
        db.create_all(app=app)
        print('Database has been created')
