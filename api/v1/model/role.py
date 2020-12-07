from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    users = db.relationship('User', secondary="role_users")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "users": self.users
        }
