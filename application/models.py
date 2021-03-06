from application import db

class orders(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable =False, unique=True)
    product = db.Column(db.String(20), nullable =False)
    collection_date_time= db.Column(db.String(100), nullable = False, unique = True) #cannot be same date and time as another order
    products_id = db.Column(db.Integer, db.ForeignKey('products.id'))
   #Wont create a column, this is python being told that there is a relationship between the two models here

class products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    orders = db.relationship('orders', backref='prod')
    