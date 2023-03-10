from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    reg_code = db.Column(db.Integer, nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, default=datetime.date.today)
    start_capital = db.Column(db.Integer, nullable=False)

    natural_shareholders = db.relationship("NaturalShareHolder", backref="company", lazy=True)
    legal_shareholders = db.relationship("LegalShareHolder", backref="company", lazy=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'reg_code': self.reg_code,
            'start_date': str(self.start_date),
            'start_capital': self.start_capital
        }

class NaturalShareHolder(db.Model):
    __tablename__ = 'natural_shareholders'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    social_insurance_number = db.Column(db.String, nullable=False)
    founder = db.Column(db.Boolean)
    shares = db.Column(db.Integer)

    company_id = db.Column(db.Integer, db.ForeignKey('companies.reg_code'), nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'social_insurance_number': self.social_insurance_number,
            'company_id': self.company_id,
            'founder': self.founder,
            'shares': self.shares
        }
    
class LegalShareHolder(db.Model):
    __tablename__ = 'legal_shareholders'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    reg_code = db.Column(db.Integer, nullable=False)
    founder = db.Column(db.Boolean)
    shares = db.Column(db.Integer)

    company_id = db.Column(db.Integer, db.ForeignKey('companies.reg_code'), nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'reg_code': self.reg_code,
            'company_id': self.company_id,
            'founder': self.founder,
            'shares': self.shares
        }
