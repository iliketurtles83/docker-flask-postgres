from flask_wtf import FlaskForm
from wtforms import StringField, DateField, DecimalField, FieldList, FormField, BooleanField, HiddenField, SubmitField
from wtforms.validators import DataRequired, ValidationError, NumberRange

class LegalShareholderForm(FlaskForm):
    leg_name = StringField('Name', validators=[DataRequired()])
    leg_reg_code = StringField('Registration Code', validators=[DataRequired()])
    leg_shares = DecimalField('Shares', validators=[DataRequired(), NumberRange(min=1)])
    leg_founder = BooleanField('Founder')
    _leg_founder_ = HiddenField('Founder', default=False)

class NaturalShareholderForm(FlaskForm):
    nat_first_name = StringField('Name', validators=[DataRequired()], description='First Name')
    nat_last_name = StringField('Last Name', validators=[DataRequired()])
    nat_sin = StringField('Social Insurance Number', validators=[DataRequired()])
    nat_shares = DecimalField('Shares', validators=[DataRequired(), NumberRange(min=1)])
    nat_founder = BooleanField('Founder')
    _nat_founder_ = HiddenField('Founder', default=False)

class CompanyForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()], description='Company Name')
    reg_code = StringField('Registration Code:', validators=[DataRequired()])
    start_date = DateField('Start Date:', validators=[DataRequired()])
    start_capital = DecimalField('Starting Capital:', validators=[DataRequired()])
    legal_shareholders = FieldList(FormField(LegalShareholderForm), min_entries=1, max_entries=5)
    natural_shareholders = FieldList(FormField(NaturalShareholderForm), min_entries=1, max_entries=5)
    submit = SubmitField('Register')

    def validate_shareholders(self, field):
        if not field.entries:
            raise ValidationError('You must add at least one shareholder')