
from flask import Blueprint, jsonify, request, render_template

from web.forms import CompanyForm
from web.models import db, Company, NaturalShareHolder, LegalShareHolder

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def hello():
    return render_template('index.html'), 200

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
    return render_template('companies.html', companies=companies), 200

@main_bp.route('/new_company', methods=['GET', 'POST'])
def create_company():
    if request.method == 'GET':
        return render_template("new_company.html", form=CompanyForm()), 200
    if request.method == 'POST':
            form = CompanyForm()
            if form.validate_on_submit():
                company = Company(
                    name=request.form['name'],
                    reg_code=request.form['reg_code'],
                    start_date=request.form['start_date'],
                    start_capital=request.form['start_capital']
                )
                db.session.add(company)

                for shareholder_form in form.legal_shareholders:
                    shareholder = LegalShareHolder(
                        name=shareholder_form.name.data,
                        reg_code=shareholder_form.reg_code.data,
                        founder=shareholder_form.founder.data,
                        shares=shareholder_form.shares.data,
                        company_id=company.reg_code
                    )
                    company.legal_shareholders.append(shareholder)
                for shareholder_form in form.natural_shareholders:
                    shareholder = NaturalShareHolder(
                        first_name=shareholder_form.first_name.data,
                        last_name=shareholder_form.last_name.data,
                        social_insurance_number=shareholder_form.social_insurance_number.data,
                        founder=shareholder_form.founder.data,
                        shares=shareholder_form.shares.data,
                        company_id=company.reg_code
                    )
                    company.natural_shareholders.append(shareholder)

                db.session.commit()
                return "Company created"
            else:
                return "Form is not valid"

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