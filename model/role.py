from manage import db


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    users = db.relationship('User', backref='role', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "users": self.users
        }
