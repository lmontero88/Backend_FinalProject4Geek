from manage import db
from sqlalchemy import ForeignKey


class Clasificado(db.Model):
    __tablename__ = 'clasificados'
    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, ForeignKey('user.id'))
    name = db.Column(db.String(100))
    date = db.Column(db.DateTime)
    description = db.Column(db.String(300), nullable=True, default="")
    condition = db.Column(db.String(100), nullable=True, default="")
    price = db.Column(db.Integer)
    # sport_id = db.Column(db.Integer, ForeignKey('sports.id'))
    # sport = db.relationship('Sport', back_populates='clasificados')
    # Favourite_Clasificado = db.relationship('Favourite_Clasificado', backref='favourite_clasificado', lazy=True)
    # user = db.relationship('User', backref='user', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "date": self.date,
            "description": self.description,
            "condition": self.condition,
            "price": self.price,
            "sport_id": self.sport_id,
            # "Favourite_Clasificado": self.Favourite_Clasificado,
            "user": self.user,
        }
