
from app import app

from flask import Flask,render_template,redirect, request , Blueprint, flash
import requests
from .forms import pokemon_info
from .forms import pokemon_info



@app.route('/')
def home():
    return render_template('home.html')

    
@app.route('/pokemon', methods=['GET','POST'])
def pokemon():
    form = pokemon_info()
    if request.method == 'POST':
        poke_name = form.pokemon_name.data
        url = f'https://pokeapi.co/api/v2/pokemon/{poke_name}'
        response = requests.get(url)
        if response.ok:
            data = response.json()
            char={}
            char['pok_name']=data['forms'][0]['name']
            char['pok_hp']=data['stats'][0]['base_stat']
            char['pok_attack']=data['stats'][1]['base_stat']
            char['pok_defense']=data['stats'][2]['base_stat']
            char['pok_ability']=(data['abilities'][0]['ability']['name'])
            char['pok_experience']=data['base_experience']
            char['pok_spirit_img']=data['sprites']['front_shiny']
            
            return render_template('pokemon.html', form=form, char=char)
        else:
            print('Please make sure you enetered the right Pokemon')
    # poke_name = name
    # url = f'https://pokeapi.co/api/v2/pokemon/{poke_name}'
    # response = requests.get(url)
    # if response.ok:
    #     data = response.json()
    #     char={}
    #     char['pok_name']=data['forms'][0]['name']
    #     char['pok_hp']=data['stats'][0]['base_stat']
    #     char['pok_attack']=data['stats'][1]['base_stat']
    #     char['pok_defense']=data['stats'][2]['base_stat']
    #     char['pok_ability']=(data['abilities'][0]['ability']['name'])
    #     char['pok_experience']=data['base_experience']
    #     char['pok_spirit_img']=data['sprites']['front_shiny']
    #     return(char)
#     else:
#         return 'Please make sure you enetered the right Pokemon'


    return render_template('pokemon.html',form=form)
