import jwt
from datetime import datetime, timedelta
from manage import db
from app import flask_bcrypt, key


class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    registered_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
    birthdate = db.Column(db.DateTime)
    #dia_hora = db.Column(db.DateTime)
    phones = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    status = db.Column(db.Boolean, default=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    photo = db.Column(db.String(100), default='without-photo.png')
    #friends = db.relationship('Friend', backref='user', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "firstname": self.first_name,
            "lastname": self.last_name,
            "email": self.email,
            # "password": self.password_hash,
            "phones": self.phones,
            "status": self.status,
            "birthdate": self.birthdate,
            "gender": self.gender,
            "role": self.role_id,
            #"dia_hora": self.dia_hora,
            "photo":self.photo,
        }

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def encode_auth_token(self):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(days=1, seconds=5),
                'iat': datetime.utcnow(),
                'sub': self.id,
                'role': self.role_id,
                'firstName': self.first_name,
                'email': self.email
            }
            return jwt.encode(
                payload,
                key,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, key)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def __repr__(self):
        return "<User '{}'>".format(self.username)
