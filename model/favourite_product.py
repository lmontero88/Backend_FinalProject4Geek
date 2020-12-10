from sqlalchemy import ForeignKey
from manage import db


class FavouriteProduct(db.Model):
    __tablename__ = 'Favourite_Product'
    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, ForeignKey('user.id'))
    # clasificados_id = db.Column(db.Integer, ForeignKey('clasificados.id'))
    # user = db.relationship('User', backref='user', lazy=True)

    def serialize(self):
        return {
            "user_id": self.user_id,
            "clasificados_id": self.clasificados_id,
            "user": self.user
        }
