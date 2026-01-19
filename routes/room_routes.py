from flask import Blueprint, request, jsonify
from services.room_service import RoomService

room_bp = Blueprint("room", __name__)


@room_bp.route("/", methods=["GET"])
def get_rooms():
    rooms = RoomService.get_all_rooms()
    return jsonify([room.to_json() for room in rooms])


@room_bp.route("/", methods=["POST"])
def create_room():
    room = RoomService.create_room(request.json)
    return jsonify(room.to_json()), 201


@room_bp.route("/<int:room_id>", methods=["PUT"])
def update_room(room_id):
    room = RoomService.update_room(room_id, request.json)
    if not room:
        return jsonify({"error": "Raum nicht gefunden"}), 404
    return jsonify(room.to_json())


@room_bp.route("/<int:room_id>", methods=["DELETE"])
def delete_room(room_id):
    success = RoomService.delete_room(room_id)
    if not success:
        return jsonify({"error": "Raum nicht gefunden"}), 404
    return jsonify({"message": "Raum gelöscht"})
