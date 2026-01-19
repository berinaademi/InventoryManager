from database import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # Dies speichert den HASH
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(120), nullable=False)

    # Beziehung: Ein Benutzer kann viele Räume haben
    rooms = db.relationship("Room", backref="owner",
                            lazy=True, cascade="all, delete-orphan")

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_json(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name
        }
