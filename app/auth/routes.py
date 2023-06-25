from flask import Blueprint ,render_template, request, redirect, url_for, flash
import requests
from .forms import SignUp
from .forms import LogIn
from ..models import User, Pokemon
from flask_login import current_user, login_user, logout_user
from werkzeug.security import check_password_hash



auth = Blueprint('auth', __name__, template_folder = 'auth_templates')  
# , url_prefix='auth')



@auth.route('/signup', methods=['GET','POST'])
def signup():
    form = SignUp()
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            #uer.query
            user = User(username, email, password)
            user.save_user()
            if username == user.username:
                flash(f"Congrats {username}", "success")
                
                return redirect(url_for('auth.login'))
                
            return redirect(url_for('auth.login'))
    return render_template('Signup.html',form=form)

@auth.route('/login', methods=['GET','POST'])
def login():
    form = LogIn()
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(username=username).first()
            if user:
                if check_password_hash(user.password, password):
                # if user.password == password: not secured
                    flash(f"welcome back {username}", 'success')
                    login_user(user)
                    return redirect(url_for('home'))
                else:
                    flash('wrong password,username', 'danger')
            else:
                flash('user doesn\'t exist', 'danger')

    return render_template('login.html', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    flash('See you later', 'primary')
    return redirect(url_for('home'))