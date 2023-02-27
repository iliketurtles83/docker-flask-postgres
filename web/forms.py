from flask_wtf import FlaskForm
from wtforms import StringField, DateField, DecimalField, FieldList, FormField
from wtforms.validators import DataRequired

class ShareholderForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    # Add any other fields needed for legal or natural shareholders

class CompanyForm(FlaskForm):
    name = StringField('Desired Name', validators=[DataRequired()])
    reg_code = StringField('Regisration Code', validators=[DataRequired()])
    start_date = DateField('Start Date', validators=[DataRequired()])
    start_capital = DecimalField('Starting Capital', validators=[DataRequired()])
    legal_shareholders = FieldList(FormField(ShareholderForm))
    natural_shareholders = FieldList(FormField(ShareholderForm))
