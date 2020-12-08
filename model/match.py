from sqlalchemy import ForeignKey
from manage import db


class Match(db.Model):
    __tablename__ = 'Match'
    id = db.Column(db.Integer, primary_key=True)
    user_to_id = db.Column(db.Integer, ForeignKey('user.id'))
    user_from_id = db.Column(db.Integer, ForeignKey('user.id'))
    #user = db.relationship('User', backref='match', lazy=True)

    def serialize(self):
        return {
            "user_to_id": self.user_to_id,
            "user_from_id": self.user_from_id,
            "user": self.user
        }
