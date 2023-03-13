
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
    if form.validate_on_submit():
        company = Company(
            name=form.name.data,
            reg_code=form.reg_code.data,
            start_date=form.start_date.data,
            start_capital=form.start_capital.data
        )
        db.session.add(company)
        db.session.commit()

        # Add natural shareholders
        for shareholder_entry in form.natural_shareholders:
            shareholder = NaturalShareHolder(
                first_name=shareholder_entry.nat_first_name.data,
                last_name=shareholder_entry.nat_last_name.data,
                social_insurance_number=shareholder_entry.nat_sin.data,
                shares=shareholder_entry.nat_shares.data,
                founder=shareholder_entry.nat_founder.data,
                company_id=company.reg_code
            )
            db.session.add(shareholder)
            db.session.commit()

        # Add legal shareholders
        for shareholder_entry in form.legal_shareholders:
            shareholder = LegalShareHolder(
                name=shareholder_entry.leg_name.data,
                reg_code=shareholder_entry.leg_reg_code.data,
                shares=shareholder_entry.leg_shares.data,
                founder=shareholder_entry.leg_founder.data,
                company_id=company.reg_code
            )
            db.session.add(shareholder)
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

@main_bp.route('/company/<int:id>/delete')
def delete_company(id):
    print('delete company')
    company = Company.query.get(id)
    if company is None:
        return jsonify({'message': 'Company not found'}), 404
    db.session.delete(company)
    db.session.commit()
    return redirect(url_for('main.get_companies'))