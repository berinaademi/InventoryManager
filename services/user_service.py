from models import user
from models.user import User
from database import db
from werkzeug.security import generate_password_hash, check_password_hash


class UserService:
    @staticmethod
    def create_user(data):
        # Prüfen, ob der Benutzer bereits existiert
        existing_user = User.query.filter_by(email=data.get("email")).first()
        if existing_user:
            return None  # Dies verhindert einen Datenbankabsturz und löst den 400-Fehler in den Routes aus
        # Passwort aus Sicherheitsgründen hashen
        hashed_pw = generate_password_hash(data.get("password"))

        user = User(
            name=data.get("name"),
            email=data.get("email"),
            password=hashed_pw
        )
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def authenticate_user(email, password):
        user = User.query.filter_by(email=email).first()

        # check_password_hash vergleicht die Texteingabe mit dem gespeicherten Hash
        if user and check_password_hash(user.password, password):
            return user
        return None

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def change_password(user_id, current_password, new_password):
        user = User.query.get(user_id)
        if not user:
            return None

        # Aktuelles Passwort verifizieren
        if not check_password_hash(user.password, current_password):
            return False  # Aktuelles Passwort ist falsch

        # Auf neues Passwort aktualisieren
        user.password = generate_password_hash(new_password)
        db.session.commit()
        return True

    @staticmethod
    def delete_user(user_id, password):
        user = User.query.get(user_id)
        if not user:
            return None

    # Passwort vor dem Löschen verifizieren
        if not check_password_hash(user.password, password):
            return False  # Passwort ist falsch

        db.session.delete(user)
        db.session.commit()
        return True
