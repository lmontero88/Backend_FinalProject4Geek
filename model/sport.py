from manage import db


class Sport(db.Model):  # hasta aca estan ok las relaciones
    __tablename__ = 'sports'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    # clasificados = db.relationship('Clasificado', backref='sport', lazy=True)
    # user_sport = db.relationship('UserSport', backref='user_sport', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "clasificado": self.clasificados,
            "user_sport": self.user_sport,
        }
