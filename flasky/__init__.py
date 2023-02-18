from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from models import db
from config import Config
from routes import init_routes
# from routes import main_bp


print('hahahaha')
def create_app(config_name=Config):
    app = Flask(__name__)

    app.config.from_object(config_name)
    # config[config_name].init_app(app)

    db.init_app(app)

    init_routes(app)

    # app.register_blueprint(main_bp)

    return app