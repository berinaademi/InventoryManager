from flask import Blueprint, request, jsonify
from services.user_service import UserService

user_bp = Blueprint("user", __name__)


@user_bp.route("/", methods=["GET"])
def get_users():
    users = UserService.get_all_users()
    return jsonify([user.to_json() for user in users])


@user_bp.route("/", methods=["POST"])
def create_user():
    data = request.json
    user = UserService.create_user(data)

    if not user:
        return jsonify({"error": "User existiert bereits oder Daten sind ungültig"}), 400

    return jsonify(user.to_json()), 201


@user_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    # Zuerst prüfen, ob der Benutzer existiert
    from models.user import User
    user_exists = User.query.filter_by(email=email).first()

    if not user_exists:
        return jsonify({"error": "Dieses Profil existiert nicht"}), 404

    # dann authentifizieren
    user = UserService.authenticate_user(email, password)

    if user:
        return jsonify(user.to_json()), 200

    return jsonify({"error": "Ungültige E-Mail oder Passwort"}), 401


@user_bp.route("/<int:user_id>/change-password", methods=["PUT"])
def change_password(user_id):
    data = request.json
    current_password = data.get("current_password")
    new_password = data.get("new_password")

    if not current_password or not new_password:
        return jsonify({"error": "Beide Passwörter sind erforderlich"}), 400

    result = UserService.change_password(
        user_id, current_password, new_password)

    if result is None:
        return jsonify({"error": "Benutzer nicht gefunden"}), 404
    elif result is False:
        return jsonify({"error": "Aktuelles Passwort ist falsch"}), 401

    return jsonify({"message": "Passwort erfolgreich geändert"}), 200


@user_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    data = request.json
    password = data.get("password")

    if not password:
        return jsonify({"error": "Passwort ist erforderlich"}), 400

    result = UserService.delete_user(user_id, password)

    if result is None:
        return jsonify({"error": "Benutzer nicht gefunden"}), 404
    elif result is False:
        return jsonify({"error": "Passwort ist falsch"}), 401

    return jsonify({"message": "Konto erfolgreich gelöscht"}), 200
