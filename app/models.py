from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Company(db.Model):
    __tablename__ = 'companies'
    reg_code = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    start_capital = db.Column(db.Integer, nullable=False)

    def to_json(self):
        return {
            'name': self.name,
            'reg_code': self.reg_code,
            'start_date': self.start_date,
            'start_capital': self.start_capital
        }

class ShareHolder(db.Model):
    __tablename__ = 'shareholders'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    person_code = db.Column(db.Integer, nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.reg_code'), nullable=False)
    founder = db.Column(db.Boolean, nullable=False)
    shares = db.Column(db.Integer, nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'person_code': self.person_code,
            'company_id': self.company_id,
            'founder': self.founder,
            'shares': self.shares
        }