from flask import Flask
from config import Config
import os

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object(Config)
    else:
        # load the test config passed in
        app.config.from_object(test_config)

    from app.main import main_bp
    app.register_blueprint(main_bp)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
