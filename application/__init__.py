from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS
from application.config import config

# it would be used as application module variable
db = SQLAlchemy()

def create_app(config_name='default'):

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    db.init_app(app)

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from models import models as models_blueprint
    app.register_blueprint(models_blueprint)

    return app

app = create_app()
