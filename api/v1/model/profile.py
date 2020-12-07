from sqlalchemy import ForeignKey
from api.v1.app import db


class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.String(300), nullable=True, default="")
    facebook = db.Column(db.String(300), nullable=True, default="")
    instagram = db.Column(db.String(300), nullable=True, default="")
    photo = db.Column(db.String(300), nullable=True, default="")
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
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
