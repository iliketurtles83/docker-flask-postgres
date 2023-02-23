from flask import Flask
from web.models import db
from web.config import Config
from web.routes import main_bp
# from flask_migrate import Migrate

def create_app(config_name=Config):
    app = Flask(__name__)

    app.config.from_object(config_name)
    # config[config_name].init_app(app)

    db.init_app(app)
    # migrate = Migrate(app, db)
    # db.create_all(app)

    app.register_blueprint(main_bp)

    return app