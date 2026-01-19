from database import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Integer, default=0)
    min_amount = db.Column(db.Integer, default=1)  # Für F32
    price = db.Column(db.Float)
    category = db.Column(db.String(50))
    expiry_date = db.Column(db.Date)  # Für F41
    room_id = db.Column(db.Integer, db.ForeignKey("room.id"), nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "amount": self.amount,
            "min_amount": self.min_amount,
            "price": self.price,
            "category": self.category,
            "expiry_date": self.expiry_date.strftime('%Y-%m-%d') if self.expiry_date else None,
            "room_id": self.room_id
        }
