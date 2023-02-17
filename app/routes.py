
from flask import jsonify, request
from models import db, Company, ShareHolder


def init_routes(app):

    @app.route('/')
    def hello():
	    return "Hello World!"
    
    @app.route('/company/list', methods=['GET'])
    def get_companies():
        companies = Company.query.all()
        return jsonify([company.to_json() for company in companies])

    @app.route('/company/<int:id>', methods=['GET'])
    def get_company(id):
        company = Company.query.get(id)
        if company is None:
            return jsonify({'message': 'Company not found'}), 404
        return jsonify(company.to_json()), 200

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

    @app.route('/company/<int:id>', methods=['PUT'])
    def update_company(id):
        if not request.json:
            return jsonify({'message': 'Bad request'}), 400
        
        company = Company.query.get(id)
        if company is None:
            return jsonify({'message': 'Company not found'}), 404
        
        company.name = request.json['name']
        company.reg_code = request.json['reg_code']
        company.start_date = request.json['start_date']
        company.start_capital = request.json['start_capital']
        db.session.commit()
        return jsonify(company.to_json())
