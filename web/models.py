from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Company(db.Model):
    __tablename__ = 'companies'
    reg_code = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    start_date = db.Column(db.Date, default=datetime.date.today)
    start_capital = db.Column(db.Integer)

    def to_json(self):
        return {
            'name': self.name,
            'reg_code': self.reg_code,
            'start_date': str(self.start_date),
            'start_capital': self.start_capital
        }

class ShareHolder(db.Model):
    __tablename__ = 'shareholders'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    person_code = db.Column(db.Integer)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.reg_code'))
    founder = db.Column(db.Boolean)
    shares = db.Column(db.Integer)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'person_code': self.person_code,
            'company_id': self.company_id,
            'founder': self.founder,
            'shares': self.shares
        }