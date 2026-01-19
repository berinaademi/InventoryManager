from models.room import Room
from database import db


class RoomService:
    @staticmethod
    def get_all_rooms():
        return Room.query.all()

    @staticmethod
    def get_room_by_id(room_id):
        return Room.query.get(room_id)

    @staticmethod
    def create_room(data):
        room = Room(
            name=data.get("name"),
            description=data.get("description"),
            user_id=data.get("user_id")
        )
        db.session.add(room)
        db.session.commit()
        return room

    @staticmethod
    def update_room(room_id, data):
        room = Room.query.get(room_id)
        if not room:
            return None
        room.name = data.get("name", room.name)
        room.description = data.get("description", room.description)
        db.session.commit()
        return room

    @staticmethod
    def delete_room(room_id):
        room = Room.query.get(room_id)
        if not room:
            return False
        db.session.delete(room)
        db.session.commit()
        return True
