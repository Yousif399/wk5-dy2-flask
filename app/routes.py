from app import app

from flask import Flask,render_template,redirect, request , Blueprint, flash, url_for
import requests
from .forms import PokemonInfo

from flask_login import login_required, current_user
from .models import Pokemon, User



@app.route('/')
def home():
    return render_template('home.html')

    
@app.route('/pokemon', methods=['GET','POST'])
@login_required
def pokemon():
    form = PokemonInfo()
    if request.method == 'POST':
        if form.validate_on_submit():
            if 'search' in request.form:
                poke_name = form.pokemon_name.data
                url = f'https://pokeapi.co/api/v2/pokemon/{poke_name}'
                response = requests.get(url)
                if response.ok:
                    data = response.json()
                    char = {}
                    char['pok_name'] = data['forms'][0]['name']
                    char['pok_hp'] = data['stats'][0]['base_stat']
                    char['pok_attack'] = data['stats'][1]['base_stat']
                    char['pok_defense'] = data['stats'][2]['base_stat']
                    char['pok_ability'] = data['abilities'][0]['ability']['name']
                    char['pok_experience'] = data['base_experience']
                    char['pok_spirit_img'] = data['sprites']['front_shiny']
                    print('its working')
                    q = Pokemon.query.filter_by(name = poke_name).first()
                    print(q)
                    if not q:
                        flash('pokemon isn\'t in the data base')
                        pokemon_data = Pokemon(char['pok_name'],char['pok_hp'],char['pok_attack'],char['pok_defense'],char['pok_spirit_img'])
                        pokemon_data.data_base()
                    p = Pokemon.query.filter_by(name = poke_name).first()
                    print(p,'yes')

                    return render_template('pokemon.html', form=form, char=char,p=p)
                else:
                    flash('Please make sure you entered the right Pokemon', 'danger')

            elif 'add' in request.form:
                poke_name = form.pokemon_name.data
                pokemon = Pokemon(poke_name, current_user.id)
                pokemon.save_pokemon()
                flash('Pokemon added successfully', 'success')
                return redirect('/profile')

        else:
            flash('Please make sure you entered the right Pokemon', 'danger')

    return render_template('pokemon.html', form=form)


# def pokemon():
#     form = PokemonInfo()
#     if request.method == 'POST':
#         poke_name = form.pokemon_name.data
#         url = f'https://pokeapi.co/api/v2/pokemon/{poke_name}'
#         response = requests.get(url)
#         if response.ok:
#             data = response.json()
#             char={}
#             char['pok_name']=data['forms'][0]['name']
#             char['pok_hp']=data['stats'][0]['base_stat']
#             char['pok_attack']=data['stats'][1]['base_stat']
#             char['pok_defense']=data['stats'][2]['base_stat']
#             char['pok_ability']=(data['abilities'][0]['ability']['name'])
#             char['pok_experience']=data['base_experience']
#             char['pok_spirit_img']=data['sprites']['front_shiny']
            
#             return render_template('pokemon.html', form=form, char=char)
#         else:
#             flash('Please make sure you enetered the right Ppppppppokemon','danger')
        
#     return render_template('pokemon.html',form=form)

@app.route('/profile', methods=['GET','POST'])
@login_required
def profile():
    return render_template('profile.html')

@app.route('/add-pok/<int:pokemon_id>', methods=['POST'])
@login_required
def add_pok(pokemon_id):
    print('helooooooo')
    pokemon = Pokemon.query.filter_by().first() #Pokemon.query.get(pokemon_id) --> I assume this is what we're going for?
    pokemon.save_pokemon(current_user)
    flash('Pokemon added successfully', 'success')
    return redirect(url_for('profile'))  

    print('noo')
    flash('Please make sure you enetered the right Pokemon','danger')                    
    return redirect('/pokemon')

# form = PokemonInfo(request.form)
    # print('pokemon_name:', form.pokemon_name.data)
    # print(form.errors)
    # if form.validate_on_submit():
    #     poke_name = form.pokemon_name.data
    #     pokemon = Pokemon(poke_name, current_user.id)
    #     print('added')



    # formm = Add_pok()
#     if request.method == 'POST':
#         # add = form.add
#     # added_pokemon = Pokemon.query.all()
#     # print(added_pokemon)
   
    
# pokemon_id = pokemon_id



 # x = pokemon()
    # form = pokemon_info()
    # poke_name= form.pokemon_name.data
    # if x:
    #     pokemon = Pokemon(poke_name,current_user.id)