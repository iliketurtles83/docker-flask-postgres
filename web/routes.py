
from flask import Blueprint, redirect, request, render_template, url_for

from web.forms import CompanyForm, LegalShareholderForm, NaturalShareholderForm
from web.models import db, Company, NaturalShareHolder, LegalShareHolder

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def hello():
    return render_template('index.html'), 200

@main_bp.route('/company/<int:id>', methods=['GET'])
def get_company(id):
    company = Company.query.get_or_404(id)

    legal_shareholders = LegalShareHolder.query.filter_by(company_id=company.id).all()
    natural_shareholders = NaturalShareHolder.query.filter_by(company_id=company.id).all()
    if legal_shareholders is not None:
         company.legal_shareholders = legal_shareholders
    if natural_shareholders is not None:
        company.natural_shareholders = natural_shareholders
    return render_template('details.html', company=company, legal_form=LegalShareholderForm(), natural_form=NaturalShareholderForm()), 200

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

        # get company id
        company = Company.query.filter_by(reg_code=form.reg_code.data).first()
        company_id = company.id

        # Add natural shareholders
        for shareholder_entry in form.natural_shareholders:
            shareholder = NaturalShareHolder(
                first_name=shareholder_entry.first_name.data,
                last_name=shareholder_entry.last_name.data,
                social_insurance_number=shareholder_entry.sin.data,
                shares=shareholder_entry.shares.data,
                founder=shareholder_entry.founder.data,
                company_id=company_id
            )
            db.session.add(shareholder)
            db.session.commit()

        # Add legal shareholders
        for shareholder_entry in form.legal_shareholders:
            shareholder = LegalShareHolder(
                name=shareholder_entry.leg_name.data,
                reg_code=shareholder_entry.reg_code.data,
                shares=shareholder_entry.shares.data,
                founder=shareholder_entry.founder.data,
                company_id=company_id
            )
            db.session.add(shareholder)
            db.session.commit()
        return redirect(url_for('main.get_company', id=company.id))
    return render_template("new_company.html", form=form), 200

@main_bp.route('/company/<int:id>/update', methods=['POST'])
def update_company(id):
    company = Company.query.get_or_404(id)
    company.name = request.form['name']
    db.session.commit()
    return redirect(url_for('main.get_company', id=company.id))

@main_bp.route('/company/<int:id>/delete')
def delete_company(id):
    company = Company.query.get_or_404(id)

    db.session.delete(company)
    db.session.commit()
    return redirect(url_for('main.get_companies'))

@main_bp.route('/company/<int:id>/add_natural', methods=['GET', 'POST'])
def add_natural_shareholder(id):
    form = NaturalShareholderForm()
    if form.validate_on_submit():
        shareholder = NaturalShareHolder(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            social_insurance_number=form.sin.data,
            shares=form.shares.data,
            founder=form.founder.data,
            company_id=id
        )
        db.session.add(shareholder)
        db.session.commit()
        return redirect(url_for('main.get_company', id=id))
    
@main_bp.route('/company/<int:id>/add_legal', methods=['GET', 'POST'])
def add_legal_shareholder(id):
    form = LegalShareholderForm()
    if form.validate_on_submit():
        shareholder = LegalShareHolder(
            name=form.leg_name.data,
            reg_code=form.reg_code.data,
            shares=form.shares.data,
            founder=form.founder.data,
            company_id=id
        )
        db.session.add(shareholder)
        db.session.commit()
        return redirect(url_for('main.get_company', id=id))

@main_bp.route('/delete_natural/<int:id>')
def delete_natural_shareholder(id):
    shareholder = NaturalShareHolder.query.get_or_404(id)
    db.session.delete(shareholder)
    db.session.commit()
    return redirect(url_for('main.get_company', id=shareholder.company_id))

@main_bp.route('/delete_legal/<int:id>')
def delete_legal_shareholder(id):
    shareholder = LegalShareHolder.query.get_or_404(id)
    db.session.delete(shareholder)
    db.session.commit()
    return redirect(url_for('main.get_company', id=shareholder.company_id))