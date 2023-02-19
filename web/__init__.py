from flask import Flask
from models import db
from config import Config
from routes import init_routes
# from routes import main_bp
# from flask_migrate import Migrate

print('in init')
def create_app(config_name=Config):
    print('in create_app')
    app = Flask(__name__)

    app.config.from_object(config_name)
    # config[config_name].init_app(app)
    # migrate = Migrate(app, db)
    db.init_app(app)

    init_routes(app)

    # app.register_blueprint(main_bp)

    return app