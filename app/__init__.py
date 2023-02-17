from flask import Flask
from config import config
from models import db


print('hahahaha')
def create_app(config_name):
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return "Hello World!"
    app.config.from_object(config.Config)
    config[config_name].init_app(app)

    db.init_app(app)
    return app