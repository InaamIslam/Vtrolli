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
        collection_date_time = form.collection_date_time

        if len(first_name) == 0 or len(last_name) == 0:
            error = 'Please supply both first and last name'
    
        def add_order():
            new_order = order_form(name = 'form.first_name.data')



        #add the info to database 
        
    return render_template('shop.html', form=form, message=error)

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

if __name__ == "__main__":
    app.run(debug=True)