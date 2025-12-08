from database import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.String(50))
    price = db.Column(db.Float)
    category = db.Column(db.String(100))
    expiry_date = db.Column(db.String(20))

    room_id = db.Column(db.Integer, db.ForeignKey("room.id"))
    room = db.relationship("Room")

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "amount": self.amount,
            "price": self.price,
            "category": self.category,
            "expiry_date": self.expiry_date,
            "room_id": self.room_id,
        }
