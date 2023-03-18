from flask_wtf import FlaskForm
from wtforms import StringField, DateField, DecimalField, FieldList, FormField, BooleanField, HiddenField, SubmitField, IntegerField
from wtforms.validators import DataRequired, ValidationError, NumberRange

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
    start_date = DateField('Start Date:', validators=[DataRequired()])
    start_capital = DecimalField('Starting Capital:', validators=[DataRequired()])
    legal_shareholders = FieldList(FormField(LegalShareholderForm), min_entries=1, max_entries=5)
    natural_shareholders = FieldList(FormField(NaturalShareholderForm), min_entries=1, max_entries=5)
    submit = SubmitField('Register')

    def validate_shareholders(self, field):
        if not field.entries:
            raise ValidationError('You must add at least one shareholder')