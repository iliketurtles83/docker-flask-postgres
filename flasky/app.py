from . import create_app
from flask import Flask
from flask_migrate import Migrate
from routes import init_routes
from models import db
import os

# app = Flask(__name__)


app = create_app()
# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URL')
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
init_routes(app)
# migrate = Migrate(app, db)
# db.init_app(app)

if __name__ == '__main__':
	with app.app_context():
		db.create_all()
		app.run(host='0.0.0.0', port=8000)