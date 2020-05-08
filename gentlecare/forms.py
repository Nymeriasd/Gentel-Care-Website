
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class ContactDeatils(FlaskForm):
    FirstName = StringField('First Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    LastName = StringField('Last Name ', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    PhoneNumber = StringField('Phone Number', validators=[DataRequired()])
    Email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=40)])
    Address = StringField('Address', validators=[DataRequired()])

    submit = SubmitField('Order')

class Maintaince(FlaskForm):
    Date = DateField('Orderdate', format='%Y-%m-%d')