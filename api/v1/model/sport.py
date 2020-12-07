from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Sport (db.Model): ##hasta aca estan ok las relaciones
    __tablename__ = 'sport'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    clasificado = db.relationship('Clasificado', back_populates = 'sport', lazy=True)
    user_sport = db.relationship('User_sport', backref = 'user_sport', lazy=True)

    def serialize(self):
        return{
            "id":self.id,
            "name":self.name,
            "clasificado":self.clasificado,
            "user_sport":self.user_sport,
        }