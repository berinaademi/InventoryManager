from flask import Blueprint, jsonify

user_bp = Blueprint("user", __name__)


@user_bp.route("/", methods=["GET"])
def test_user():
    return jsonify({"message": "User endpoint works"})
