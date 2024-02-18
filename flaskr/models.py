from . import db
from sqlalchemy.sql import func

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    itemName = db.Column(db.String(1000), unique=True)
    price = db.Column(db.Float)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    products = db.relationship('Product')

# one-to-many
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000), unique=True)
    price = db.Column(db.Float)
    image = db.Column(db.String)
    url = db.Column(db.String)
    item_id = db.column(db.Integer, db.ForeignKey('item.id'))