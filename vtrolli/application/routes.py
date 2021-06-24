# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# @app.route('/home')
# def home():
#     return 'WELCOME TO VTROLLI'

# @app.route('/shop')
# def shop():
#     return 'Select your items from the list of products below, then select your preferred collection time.'

# @app.route('/checkout')
# def checkout():
#     return 'Your order details are below. Please confirm and process.'

# if __name__ == "__main__":
#     app.run(debug=True)

###Adding the routes with HTML files

from flask import Flask, render_template, request
from application import app
from application.forms import order_form
import datetime 

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/shop', methods=['GET', 'POST'])
def shop():
    error = ""
    form = order_form()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        product = form.product.data
        collection_date_time = form.collection_date_time.data

        # if len(first_name) == 0 or len(last_name) == 0:
        #     error = 'Please supply both first and last name'
        # if len(email) == 0:
        #     error = 'Please insert an email address so that we can update you regard your order'
        # if len(collection_date_time) == 0: 
        #     error = 'Please state enter your preffered date and time for collection'
        # if #no selection for the product 

    
        def add_order():
            new_order = order_form(
                first_name = 'form.first_name.data', last_name = 'form.last_name.data', 
                email = 'form.email.data',
                product = 'form.product.data',
                collection_date_time = 'form.collection_date_time.data')
            db.session.add(new_order)
            db.session.commit()
            return "Added new order to database"
       

        #add the info to database 
        
    return render_template('shop.html', form=form, message=error)

@app.route('/checkout')

def read_order():
     all_orders = order_form.query.all()
     my_order = ""
     for order in all_orders:
         order_string += "<br>"+ order.name






# def order_checkout():
#     return print(new_order)

# def update_order():
#     new_order = order.query.first()
#     first 

# def delete_order():

def checkout():
    return render_template('checkout.html')

if __name__ == "__main__":
    app.run(debug=True)