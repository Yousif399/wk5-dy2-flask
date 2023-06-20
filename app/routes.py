
from app import app

from flask import Flask,render_template,redirect, request , Blueprint
import requests
from .forms import pokemon_info
from .forms import pokemon_info



@app.route('/')
def home():
    return render_template('home.html')

    
@app.route('/pokemon', methods=['GET','POST'])
def pokemon():
    form = pokemon_info()
#     poke_name = name
#     if request.method == 'POST':

#     url = f'https://pokeapi.co/api/v2/pokemon/{poke_name} '
#     response = requests.get(url)
#     if response.ok:
#         data = response.json()
#         char={}
#         char['pok_name']=data['forms'][0]['name']
#         char['pok_ability']=(data['abilities'][0]['ability']['name'])
#         char['pok_experience']=data['base_experience']
#         char['pok_spirit_img']=data['sprites']['front_shiny']
#         return char
#     else:
#         return 'Please make sure you enetered the right Pokemon'

    return render_template('pokemon.html',form=form)
