from flask import Blueprint, request, jsonify
from services.item_service import ItemService

item_bp = Blueprint("item", __name__)


@item_bp.route("/", methods=["GET"])
def get_items():
    return jsonify([i.to_json() for i in ItemService.get_all_items()])


@item_bp.route("/", methods=["POST"])
def create_item():
    item = ItemService.create_item(request.json)
    return jsonify(item.to_json()), 201


@item_bp.route("/shopping-list", methods=["GET"])
def shopping_list():
    items = ItemService.get_low_stock_items()
    return jsonify([i.to_json() for i in items])


@item_bp.route("/expiring", methods=["GET"])
def expiring():
    days = request.args.get('days', 7, type=int)
    items = ItemService.get_expiring_soon(days)
    return jsonify([i.to_json() for i in items])


@item_bp.route("/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = ItemService.update_item(item_id, request.json)
    if not item:
        return jsonify({"error": "Artikel nicht gefunden"}), 404
    return jsonify(item.to_json())


@item_bp.route("/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    success = ItemService.delete_item(item_id)
    if not success:
        return jsonify({"error": "Artikel nicht gefunden"}), 404
    return jsonify({"message": "Artikel gelöscht"})
