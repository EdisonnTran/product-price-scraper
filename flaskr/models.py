from . import db
from sqlalchemy.sql import func

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    itemName = db.Column(db.String(1000), unique=True)
    price = db.Column(db.Float)
    date = db.Column(db.DateTime(timezone=True), default=func.now())