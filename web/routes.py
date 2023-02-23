
from flask import Blueprint, jsonify, request, render_template

from web.models import db, Company, NaturalShareHolder, LegalShareHolder

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def hello():
    companies = Company.query.all()
    return render_template('index.html', companies=companies), 200

@main_bp.route('/company/<int:id>', methods=['GET'])
def get_company(id):
    company = Company.query.get(id)
    if company is None:
        return jsonify({'message': 'Company not found'}), 404
    legal_shareholders = LegalShareHolder.query.filter_by(company_id=company.reg_code).all()
    natural_shareholders = NaturalShareHolder.query.filter_by(company_id=company.reg_code).all()
    if legal_shareholders is not None:
         company.legal_shareholders = legal_shareholders
    if natural_shareholders is not None:
        company.natural_shareholders = natural_shareholders
    return render_template('details.html', company=company), 200

@main_bp.route('/company/list', methods=['GET'])
def get_companies():
    companies = Company.query.all()
    return jsonify([company.to_json() for company in companies])

@main_bp.route('/company', methods=['POST'])
def create_company():
    if not request.json:
        return jsonify({'message': 'Bad request'}), 400
    
    company = Company(
        name=request.json['name'],
        reg_code=request.json['reg_code'],
        start_capital=request.json['start_capital']
    )
    db.session.add(company)
    db.session.commit()
    return jsonify(company.to_json()), 201

@main_bp.route('/company/<int:id>', methods=['PUT'])
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