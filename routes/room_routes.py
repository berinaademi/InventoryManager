from flask import Blueprint, request, jsonify
from database import db
from models.room import Room

room_bp = Blueprint("room", __name__)


@room_bp.route("/", methods=["GET"])
def get_rooms():
    rooms = Room.query.all()
    return jsonify([room.to_json() for room in rooms]), 200


@room_bp.route("/<int:id>", methods=["GET"])
def get_room(id):
    room = Room.query.get_or_404(id)
    return jsonify(room.to_json()), 200


@room_bp.route("/", methods=["POST"])
def create_room():
    data = request.json
    new_room = Room(
        name=data.get("name"),
        description=data.get("description")
    )
    db.session.add(new_room)
    db.session.commit()

    return jsonify(new_room.to_json()), 201


@room_bp.route("/<int:id>", methods=["PUT"])
def update_room(id):
    room = Room.query.get_or_404(id)
    data = request.json

    room.name = data.get("name", room.name)
    room.description = data.get("description", room.description)

    db.session.commit()

    return jsonify(room.to_json()), 200


@room_bp.route("/<int:id>", methods=["DELETE"])
def delete_room(id):
    room = Room.query.get_or_404(id)

    db.session.delete(room)
    db.session.commit()

    return jsonify({"message": "Raum gelöscht"}), 200
