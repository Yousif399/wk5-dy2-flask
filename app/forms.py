from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class PokemonInfo(FlaskForm):
    pokemon_name = StringField('Name', validators=[DataRequired()])
    search = SubmitField()
    add = SubmitField('Add')


# class Add_pok(FlaskForm):
   
