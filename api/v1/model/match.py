from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.schema import ForeignKey
db = SQLAlchemy()

class Match(db.Model):
    __tablename__ = 'Match'
    id = db.Column(db.Integer, primary_key=True)
    user_to_id = db.Column(db.Integer, ForeignKey('users.id'))
    user_from_id = db.Column(db.Integer, ForeignKey('users.id'))
    user = db.relationship('User', backref= 'user', lazy=True)

    def serialize(self):
        return{
            "user_to_id":self.user_to_id,
            "user_from_id":self.user_from_id,
            "user":self.user
        }