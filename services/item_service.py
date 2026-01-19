from models.item import Item
from database import db
from datetime import datetime, timedelta


class ItemService:
    @staticmethod
    def get_all_items():
        return Item.query.all()

    @staticmethod
    def create_item(data):
        # Schutz vor Importen & Raum-Validierung
        from models.room import Room
        if not Room.query.get(data.get("room_id")):
            return None

        # Datums-Parsing mit Fehlerbehandlung
        expiry = None
        if data.get("expiry_date"):
            try:
                expiry = datetime.strptime(
                    data.get("expiry_date"), '%Y-%m-%d').date()
            except (ValueError, TypeError):
                expiry = None

        # Sicherstellen, dass Zahlen tatsächlich Zahlen sind
        try:
            amount = int(data.get("amount", 0))
            min_amount = int(data.get("min_amount", 1))
            price = float(data.get("price", 0.0)) if data.get("price") else 0.0
        except (ValueError, TypeError):
            amount = 0
            min_amount = 1
            price = 0.0

        item = Item(
            name=data.get("name"),
            amount=amount,
            min_amount=min_amount,
            price=price,
            category=data.get("category"),
            expiry_date=expiry,
            room_id=data.get("room_id")
        )

        db.session.add(item)
        db.session.commit()
        return item

    @staticmethod
    def get_low_stock_items():
        return Item.query.filter(Item.amount <= Item.min_amount).all()

    @staticmethod
    def get_expiring_soon(days=7):
        today = datetime.now().date()
        future = today + timedelta(days=days)
        return Item.query.filter(Item.expiry_date >= today, Item.expiry_date <= future).all()

    @staticmethod
    def update_item(item_id, data):
        item = Item.query.get(item_id)
        if not item:
            return None

        # Felder aktualisieren
        item.name = data.get("name", item.name)
        item.amount = data.get("amount", item.amount)
        item.min_amount = data.get("min_amount", item.min_amount)
        item.price = data.get("price", item.price)
        item.category = data.get("category", item.category)

        # Ablaufdatum behandeln
        if data.get("expiry_date"):
            try:
                item.expiry_date = datetime.strptime(
                    data.get("expiry_date"), '%Y-%m-%d').date()
            except (ValueError, TypeError):
                pass

        db.session.commit()
        return item

    @staticmethod
    def delete_item(item_id):
        item = Item.query.get(item_id)
        if not item:
            return False
        db.session.delete(item)
        db.session.commit()
        return True
