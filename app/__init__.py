from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True, static_folder='static')

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object(Config)
    else:
        # load the test config passed in
        app.config.from_object(test_config)

    db.init_app(app)
    migrate.init_app(app,db)
    login.init_app(app)

    from app.main import main_bp
    app.register_blueprint(main_bp)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from app.models import User, Post

    # Add db and model variables to 'flask shell' context
    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'User': User, 'Post': Post}

    return app
