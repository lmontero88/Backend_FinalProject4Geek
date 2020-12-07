from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from sqlalchemy.sql.schema import ForeignKey
db = SQLAlchemy()


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    users = db.relationship('User', secondary="role_users")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "users": self.users
        }


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    birthdate = db.Column(db.Init(50))
    profile = db.relationship('Profile', backref="user", lazy=True, uselist=False)
    phones = db.relationship('Phone', backref="user", lazy=True)
    region = db.Column(db.String(100))
    comuna = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    status = active = db.Column(db.Boolean, default=True)
    role = db.relationship('Role', secondary="role_users")

    def serialize(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "password": self.password,
            "profile": self.profile.serialize(),
            "phones": self.phones,
            "status": self.status,
            "birthdate": self.birthdate,
            "region": self.region,
            "comuna": self.comuna,
            "gender": self.gender,
            "role": self.role
        }


class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.String(300), nullable=True, default="")
    facebook = db.Column(db.String(300), nullable=True, default="")
    instagram = db.Column(db.String(300), nullable=True, default="")
    photo = db.Column(db.String(300), nullable=True, default="")
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    user = db.relationship('User', secondary="user")

    def serialize(self):
        return {
            "id": self.id,
            "bio": self.bio,
            "facebook": self.facebook,
            "instagram": self.instagram,
            "photo": self.photo,
            "user_id": self.user_id,
            "user": self.user
        }
class Clasificado(db.Model):
    __tablename__ = 'clasificados'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'), primary_key=True)
    name = db.Column(db.String(100))
    date = db.Column(db.DateTime)
    description = db.Column(db.String(300), nullable=True, default="")
    condition = db.Column(db.String(100), nullable=True, default="")
    price = db.Column(db.Integer)
    sport_id = db.Column(db.Integer, ForeignKey('sport.id'))
    Favourite_Product = db.relationship('Favourite_Product', backref='favourite_product', lazy=True)
    user = db.relationship('User', backref='user', lazy=True)

    def serialize(self):
        return{
            "id":self.id,
            "user_id":self.user_id,
            "name":self.name,
            "date":self.date,
            "description":self.description,
            "condition":self.condition,
            "price":self.price,
            "sport_id":self.sport_id,
            "Favourite_Product":self.Favourite_Product,
            "user":self.user,
        }
class FavouriteProduct (db.Model):
    __tablename__ = 'Favourite_Product'
    user_id = db.Column(db.Integer,  ForeignKey('user.id'))
    product_id = db.Column(db.Integer,  ForeignKey('product.id'))
    user = db.relationship('User', backref = 'user', lazy=True)

    def serialize(self):
        return{
            "user_id":self.user_id,
            "product_id":self.product_id,
            "user":self.user
        }


class FavouriteUser(db.Model):
    __tablename__ = 'Favourite_User'
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    professor_id = db.Column(db.Integer, ForeignKey('users.id'))
    user = db.relationship('User', backref='user', lazy=True)

    def serialize(self):
        return{
            "user_id":self.user_id,
            "professor_id":self.professor_id,
            "user":self.user
        }
class Sport (db.Model): ##hasta aca estan ok las relaciones
    __tablename__ = 'Sports'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    clasificado = db.relationship('Clasificado', backref = 'sport', lazy=True)
    user_sport = db.relationship('User_sport', backref = 'user_sport', lazy=True)

    def serialize(self):
        return{
            "id":self.id,
            "name":self.name,
            "clasificado":self.clasificado,
            "user_sport":self.user_sport,
        }
class UserSport(db.Model):
    __tablename__ = 'User_Sports'
    id = db.Column(db.Integer, primary_key=True)
    experiencia = db.Column(db.String(100), nullable=True, default="")
    user_id = db.Column(db.Integer, ForeignKey('users.id'), primary_key=True)
    sport_id = db.Column(db.Integer, ForeignKey())
    sport = db.relationship('UserSport', backref = 'sport', lazy=True)
    user = db.relationship('User', backref= 'user', lazy=True)

    def serialize(self):
        return{
            "id":self.id,
            "experiencia":self.experiencia,
            "user_id":self.user_id,
            "sport_id":self.sport_id,
            "sport":self.sport,
            "user":self.user
        }
class Match(db.Model):
    __tablename__ = 'Match'
    user_to_id = db.Column(db.Integer, ForeignKey('users.id'), primary_key=True)
    user_from_id = db.Column(db.Integer, ForeignKey('users.id'), primary_key=True)
    user = db.relationship('User', backref= 'user', lazy=True)

    def serialize(self):
        return{
            "user_to_id":self.user_to_id,
            "user_from_id":self.user_from_id,
            "user":self.user
        }
#Functions
def save(self):
        db.session.add(self)
        db.session.commit()


def update(self):
    db.session.commit()


def delete(self):
    db.session.delete(self)
    db.session.commit()

#no hacer hasta saber que funcion le voy a otortgar a cada tabla