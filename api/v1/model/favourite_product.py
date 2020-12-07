from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.schema import ForeignKey
db = SQLAlchemy()

class FavouriteProduct (db.Model):
    __tablename__ = 'Favourite_Product'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,  ForeignKey('user.id'))
    product_id = db.Column(db.Integer,  ForeignKey('product.id'))
    user = db.relationship('User', backref = 'user', lazy=True)

    def serialize(self):
        return{
            "user_id":self.user_id,
            "product_id":self.product_id,
            "user":self.user
        }