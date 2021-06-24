from application import db
from application.models import orders, product

db.drop_all()
db.create_all()

order1 = orders(full_name = 'John Milner', address = '4 hartdfor house')

db.session.add(order1)
db.session.commit()

Product1 = product(item = 'Chicken', cost = '10')
Product2 = product(item = 'Cow', cost = '200')
Product3 = product(item = 'Sheep', cost = '100')
Product4 = product(item = 'Lamb', cost = '100')
Product5 = product(item = 'Fish', cost = '200')

db.session.add(Product1, Product2, Product3, Product4, Product5)
db.session.commit()

