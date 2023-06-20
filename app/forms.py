from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class pokemon_info(FlaskForm):
    pokemon_name = StringField('name', validators=[DataRequired()])
    search = SubmitField()