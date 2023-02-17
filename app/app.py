# from app import create_app
from flask import Flask
# from routes import init_routes
from models import Company, ShareHolder
import os
from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# init_routes(app)
db = SQLAlchemy(app)
# db.init_app(app)

@app.route('/')
def hello():
	return "Hello World!"

@app.route('/company', methods=['POST'])
def create_company():
	if not request.json:
		return jsonify({'message': 'Bad request'}), 400
	
	company = Company(
		name=request.json['name'],
		reg_code=request.json['reg_code'],
		start_date=request.json['start_date'],
		start_capital=request.json['start_capital']
	)
	db.session.add(company)
	db.session.commit()
	return jsonify(company.to_json()), 201

if __name__ == '__main__':
	with app.app_context():
		db.create_all()
		app.run(host='0.0.0.0', port=8000)