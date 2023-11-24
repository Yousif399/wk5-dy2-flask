from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
db = SQLAlchemy()


adds = db.Table(
    'adds',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False),
    db.Column('pokemon_id',db.Integer, db.ForeignKey('pokemon.id'), nullable=False)
)


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
    name = db.Column(db.String, nullable=False, unique=True,)
    added = db.relationship('User',
            secondary = 'adds',
            backref = 'added',
            lazy = 'dynamic'
            )

    def __init__(self,name,user_id):
        self.name=name
        self.user_id = user_id
    
    def save_pokemon(self,user):
        # db.session.add(self)
        self.added.append(user)
        db.session.commit()

    def data_base(self):
        db.session.add(self)
        db.session.commit()

        
      #add these to the pok class   
    def __init__(self,name,hp,attack,defense,img):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.img = img
        
        
        
    