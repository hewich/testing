from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField, BooleanField, TimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo



class RegistrationForm(FlaskForm):
    name = StringField('full name', validators = [DataRequired()])
    email=StringField('Email', validators=[DataRequired(), Email()])
    password=PasswordField('password', validators=[DataRequired()])
    confirm_password=PasswordField('confirm_password', validators=[DataRequired(),EqualTo('[password]')])
    submit  = SubmitField('sign up')


class LogInForm(FlaskForm):
        email=StringField('Email', validators=[DataRequired(), Email()])
        password=PasswordField('password', validators=[DataRequired()])
        remember = BooleanField('remember me')
        submit  = SubmitField('login',validators=[DataRequired()])

class AddForm(FlaskForm):
      title = StringField('title of task', validators=[DataRequired()])
      details = StringField('details of task')
      time = TimeField('due date of task', validators=[DataRequired()])
      submit=SubmitField('save')
