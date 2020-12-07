import jwt
from datetime import datetime
from api.v1.app import db, flask_bcrypt
from api.v1.config import key


class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    registered_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    public_id = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(50), unique=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    birthdate = db.Column(db.DateTime)
    profile = db.relationship('Profile', backref="user", lazy=True, uselist=False)
    phones = db.relationship('Phone', backref="user", lazy=True)
    region = db.Column(db.String(100))
    comuna = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    dia_hora = db.Column(db.DateTime)
    status = db.Column(db.Boolean, default=True)
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
            "role": self.role,
            "dia_hora":self.dia_hora
        }

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    @staticmethod
    def encode_auth_token(user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
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
