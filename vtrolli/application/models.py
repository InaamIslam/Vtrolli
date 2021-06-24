from application import db

class order(db.orders):
    id = db.Column(db.Integer, primary_key=True) #it will auto-increment
    full_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable =False, unique=True)

class product(db.product):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))