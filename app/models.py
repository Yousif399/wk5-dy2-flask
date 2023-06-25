from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    post = db.relationship('Post', backref='pok User', lazy=True)


    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
    
    def save_user(self):
        db.session.add(self)
        db.session.commit()
        

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.String)
    img_url = db.Column(db.String)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id =db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self,title,body,img_url,user_id):
        self.title = title
        self.body = body
        self.img_url = img_url
        self.user_id = user_id

    def save_user(self):
        db.session.add(self)
        db.session.commit()



class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=False)
   
    user_id =db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self,name,user_id):
        self.name=name
        self.user_id = user_id
    
    def save_pokemon(self):
        db.session.add(self)
        db.session.commit()
        
        
        
        
         # hp = db.Column(db.String, nullable=False, unique=True)
    # attack = db.Column(db.String, nullable=False, unique=True)
    # defence = db.Column(db.String, nullable=False, unique=True)