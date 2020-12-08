from sqlalchemy import ForeignKey
from manage import db


class FavouriteUser(db.Model):
    __tablename__ = 'Favourite_User'
    id = db.Column(db.Integer, primary_key=True)

    # user_id = db.Column(db.Integer, ForeignKey('user.id'))
    # professor_id = db.Column(db.Integer, ForeignKey('user.id'))
    # user = db.relationship('User', backref='user', lazy=True)

    def serialize(self):
        return {
            "user_id": self.user_id,
            "professor_id": self.professor_id,
            "user": self.user
        }
