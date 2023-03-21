from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import datetime
import bcrypt

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

    def get_id(self):
        return self.id
    
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def get_company_id(self):
        return self.company_id

class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    reg_code = db.Column(db.Integer, nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, default=datetime.date.today)
    start_capital = db.Column(db.Integer, nullable=False)

    natural_shareholders = db.relationship("NaturalShareHolder", backref="company", lazy=True, cascade="all, delete-orphan")
    legal_shareholders = db.relationship("LegalShareHolder", backref="company", lazy=True, cascade="all, delete-orphan")

class NaturalShareHolder(db.Model):
    __tablename__ = 'natural_shareholders'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    social_insurance_number = db.Column(db.String, nullable=False)
    founder = db.Column(db.Boolean)
    shares = db.Column(db.Integer)

    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
    
class LegalShareHolder(db.Model):
    __tablename__ = 'legal_shareholders'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    reg_code = db.Column(db.Integer, nullable=False)
    founder = db.Column(db.Boolean)
    shares = db.Column(db.Integer)

    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
