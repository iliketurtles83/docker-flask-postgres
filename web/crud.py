''' CRUD for SQLAlchemy models '''
#web/crud.py

from web.models import db, Company, NaturalShareHolder, LegalShareHolder

def get_companies():
    return Company.query.all()

def get_company(id):
    return Company.query.get(id)

def get_naturalshareholders(reg_code):
    return NaturalShareHolder.query.filter_by(reg_code=reg_code).all()

def get_legalshareholders(reg_code):
    return LegalShareHolder.query.filter_by(reg_code=reg_code).all()

