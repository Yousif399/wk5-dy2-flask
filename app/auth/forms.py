from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class SignUp(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Passowrd', validators=[DataRequired()])
    confirm_passowrd = PasswordField('Confirm Passowrd', validators=[DataRequired(), EqualTo('password')])
    Sign_UP = SubmitField()

class LogIn(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Passowrd', validators=[DataRequired()])
    Log_IN = SubmitField()

