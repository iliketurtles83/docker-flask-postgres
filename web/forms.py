from flask_wtf import FlaskForm
from datetime import date
from wtforms import StringField, DateField, DecimalField, FieldList, FormField, BooleanField, HiddenField, SubmitField, IntegerField, PasswordField
from wtforms.validators import DataRequired, ValidationError, NumberRange

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class LegalShareholderForm(FlaskForm):
    leg_name = StringField('Name', validators=[DataRequired()])
    reg_code = StringField('Registration Code', validators=[DataRequired()])
    shares = DecimalField('Shares', validators=[DataRequired(), NumberRange(min=1)])
    founder = BooleanField('Founder')
    _founder_ = HiddenField('Founder', default=False)

class NaturalShareholderForm(FlaskForm):
    first_name = StringField('Name', validators=[DataRequired()], description='First Name')
    last_name = StringField('Last Name', validators=[DataRequired()])
    sin = IntegerField('Social Insurance Number', validators=[DataRequired()])
    shares = DecimalField('Shares', validators=[DataRequired(), NumberRange(min=1)])
    founder = BooleanField('Founder')
    _founder_ = HiddenField('Founder', default=False)

class CompanyForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()], description='Company Name')
    reg_code = IntegerField('Registration Code:', validators=[DataRequired()])
    creator_id = IntegerField('Creator ID:', validators=[DataRequired()])
    start_date = DateField('Start Date:', validators=[DataRequired()])
    start_capital = DecimalField('Starting Capital:', validators=[DataRequired(), NumberRange(min=1)])
    legal_shareholders = FieldList(FormField(LegalShareholderForm), min_entries=1, max_entries=5)
    natural_shareholders = FieldList(FormField(NaturalShareholderForm), min_entries=1, max_entries=5)
    submit = SubmitField('Register')

    def validate_start_date(self, field):
        if field.data > date.today():
            raise ValidationError('Start Date cannot be in the future')

    def validate_natural_shareholders(self, field):
        if not field.entries:
            raise ValidationError('You must add at least one shareholder')