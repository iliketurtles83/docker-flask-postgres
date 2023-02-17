# from app import create_app
from flask import Flask
from routes import init_routes
from models import db
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# app = create_app('default')
init_routes(app)
db.init_app(app)

if __name__ == '__main__':
	with app.app_context():
		db.create_all()
		app.run(host='0.0.0.0', port=8000)