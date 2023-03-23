from flask_bootstrap import Bootstrap5
from flask import Flask
from flask_wtf import CSRFProtect
from project.models import db, User
from project.config import Config
from project.routes import main_bp
from project.auth import auth
from flask_login import LoginManager

csrf = CSRFProtect()

def create_app(config_name=Config):
    app = Flask(__name__)
    app.config.from_object(config_name)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    csrf.init_app(app)
    db.init_app(app)
    Bootstrap5(app)
    app.register_blueprint(main_bp)
    app.register_blueprint(auth)

    return app

app = create_app()