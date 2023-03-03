
from flask import Blueprint, jsonify, redirect, request, render_template, url_for

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
    form = CompanyForm()
    print(form.name.data)
    if form.validate_on_submit():
        company = Company(
            name=form.name.data,
            reg_code=form.reg_code.data,
            start_date=form.start_date.data,
            start_capital=form.start_capital.data
        )
        print(request.form.getlist('nat_first_name[]'))
        # Add natural shareholders
        nat_first_names = request.form.getlist('nat_first_name[]')
        nat_last_names = request.form.getlist('nat_last_name[]')
        nat_social_insurance_numbers = request.form.getlist('nat_sin[]')
        nat_founders = request.form.getlist('nat_founder[]')
        nat_shares = request.form.getlist('nat_shares[]')

        for i in range(len(nat_first_names)):
            natural_shareholder = NaturalShareHolder(
                first_name=nat_first_names[i],
                last_name=nat_last_names[i],
                social_insurance_number=nat_social_insurance_numbers[i],
                founder=nat_founders[i],
                shares=nat_shares[i]
            )
            company.natural_shareholders.append(natural_shareholder)

        # Add legal shareholders
        leg_names = request.form.getlist('leg_name[]')
        leg_reg_codes = request.form.getlist('leg_reg_code[]')
        leg_founders = request.form.getlist('leg_founder[]')
        leg_shares = request.form.getlist('leg_shares[]')
        
        for i in range(len(leg_names)):
            legal_shareholder = LegalShareHolder(
                name=leg_names[i],
                reg_code=leg_reg_codes[i],
                founder=leg_founders[i],
                shares=leg_shares[i]
            )
            company.legal_shareholders.append(legal_shareholder)

        db.session.add(company)
        db.session.commit()
        return redirect(url_for('main.get_company', id=company.id))
    return render_template("new_company.html", form=form), 200

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