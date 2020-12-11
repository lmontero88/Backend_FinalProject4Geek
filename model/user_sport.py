from sqlalchemy import ForeignKey
from manage import db


class UserSport(db.Model):
    __tablename__ = 'User_Sport'
    id = db.Column(db.Integer, primary_key=True)
    experiencia = db.Column(db.String(100), nullable=True, default="")
    user_id = db.Column(db.Integer, ForeignKey('user.id'), primary_key=True)
    sport_id = db.Column(db.Integer, ForeignKey('sport.id'), primary_key=True)

    # user = db.relationship('User', backref='user', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "experiencia": self.experiencia,
            "user_id": self.user_id,
            "sport_id": self.sport_id,
            "sport": self.sport.serialize()
        }