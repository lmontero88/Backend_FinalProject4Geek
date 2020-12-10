from sqlalchemy import ForeignKey
from manage import db


class Friend(db.Model):
    __tablename__ = 'Friend'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    friend_id = db.Column(db.Integer, ForeignKey('user.id'))

    def serialize(self):
        return {
            "user_to_id": self.user_to_id,
            "user_from_id": self.user_from_id,
            "user": self.user
        }
