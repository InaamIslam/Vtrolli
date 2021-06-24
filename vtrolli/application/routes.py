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

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

if __name__ == "__main__":
    app.run(debug=True)