from app import db
from sqlalchemy.sql import func

class Item(db.Model):
    itemName = db.Column(db.String(128), unique=True)
    price = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=func.now())

    def __init__(self, itemName, price):
        self.itemName = itemName
        self.price = price