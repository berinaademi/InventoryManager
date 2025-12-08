from flask import Blueprint, request, jsonify
from database import db
from models.item import Item

item_bp = Blueprint("item", __name__)


@item_bp.route("/", methods=["GET"])
def get_items():
    items = Item.query.all()
    return jsonify([item.to_json() for item in items]), 200


@item_bp.route("/<int:id>", methods=["GET"])
def get_item(id):
    item = Item.query.get_or_404(id)
    return jsonify(item.to_json()), 200


@item_bp.route("/", methods=["POST"])
def create_item():
    data = request.json
    new_item = Item(
        name=data.get("name"),
        amount=data.get("amount"),
        price=data.get("price"),
        category=data.get("category"),
        expiry_date=data.get("expiry_date"),
        room_id=data.get("room_id")
    )

    db.session.add(new_item)
    db.session.commit()

    return jsonify(new_item.to_json()), 201


@item_bp.route("/<int:id>", methods=["PUT"])
def update_item(id):
    item = Item.query.get_or_404(id)
    data = request.json

    item.name = data.get("name", item.name)
    item.amount = data.get("amount", item.amount)
    item.price = data.get("price", item.price)
    item.category = data.get("category", item.category)
    item.expiry_date = data.get("expiry_date", item.expiry_date)
    item.room_id = data.get("room_id", item.room_id)

    db.session.commit()

    return jsonify(item.to_json()), 200


@item_bp.route("/<int:id>", methods=["DELETE"])
def delete_item(id):
    item = Item.query.get_or_404(id)

    db.session.delete(item)
    db.session.commit()

    return jsonify({"message": "Item deleted"}), 200
