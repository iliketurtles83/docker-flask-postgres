from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
# from routes import init_routes
from routes import main_bp

db = SQLAlchemy()


print('hahahaha')
def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # db.init_app(app)

    # init_routes(app)

    app.register_blueprint(main_bp)

    return app