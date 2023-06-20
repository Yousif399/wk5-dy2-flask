from flask import Blueprint ,render_template, request, redirect, url_for
import requests
from .forms import SignUp
from .forms import LogIn
from ..models import User
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
            user = User(username, email, password)
            user.save_user()
            if username == username:
                print('username is used')
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
            print(user)
            if user:
                print(user.password)
                if check_password_hash(user.password, password):
                # if user.password == password: not secured
                    print(f"welcome back {username}")
                    login_user(user)
                    return redirect(url_for('home'))
                else:
                    print('wrong password')
            else:
                print('user doesn\'t exist')

    return render_template('login.html', form=form)


@auth.route('/logout')
def logout():
    return redirect(url_for('home'))