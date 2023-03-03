from flask_wtf import FlaskForm
from wtforms import StringField, DateField, DecimalField, FieldList, FormField, BooleanField, HiddenField
from wtforms.validators import DataRequired

class LegalShareholderForm(FlaskForm):
    leg_name = StringField('Name', validators=[DataRequired()])
    leg_reg_code = StringField('Registration Code', validators=[DataRequired()])
    leg_founder = BooleanField('Founder')
    _leg_founder_ = HiddenField('Founder', default=False)
    leg_shares = DecimalField('Shares', validators=[DataRequired()])

class NaturalShareholderForm(FlaskForm):
    nat_first_name = StringField('Name', validators=[DataRequired()], description='First Name')
    nat_last_name = StringField('Last Name', validators=[DataRequired()])
    nat_sin = StringField('Social Insurance Number', validators=[DataRequired()])
    nat_founder = BooleanField('Founder')
    _nat_founder_ = HiddenField('Founder', default=False)
    nat_shares = DecimalField('Shares', validators=[DataRequired()])

class CompanyForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()], description='Company Name')
    reg_code = StringField('Registration Code:', validators=[DataRequired()])
    start_date = DateField('Start Date:', validators=[DataRequired()])
    start_capital = DecimalField('Starting Capital:', validators=[DataRequired()])
    legal_shareholders = FieldList(FormField(LegalShareholderForm))
    natural_shareholders = FieldList(FormField(NaturalShareholderForm))
