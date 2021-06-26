from flask import Flask, render_template, request
from application import app
from application.forms import order_form
from application.models import orders, products
# import datetime #no longer in use, collection_date_time changed to string

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
        # new_order = orders(first_name, last_name, email, product, collection_date_time)
        # ^why does this not work? 
        new_order = orders(
            first_name = form.first_name.data, last_name = form.last_name.data, 
            email = form.email.data,
            product = form.product.data,
            collection_date_time = form.collection_date_time.data)
        db.session.add(new_order)
        db.session.commit()

        #query for the new order and then pass that thriough to the checkout
        confirmation_order = orders.query.get(new_order)
        return redirect(url_for('checkout', confirmation_order = new_order)) #add the info to database 
    return render_template('shop.html', form=form, message=error)

#when have
    #If validators are correct then send to checkout page with list of items displayed

@app.route('/checkout/<id>', methods=['GET', 'POST'])
def checkout(id): #     #read the order placed on shop
    my_order = orders.query.filter_by(id=id).first()
    
#     #if customer is happy with order, they confirm, if not can update or delete
#     #second form for updating here
#     #two buttons update and delete 
#     #delete button for delete order
    return render_template('checkout.html', myorder = my_order, form=form, message=error)
  
    

# @app.route('/update/<id>', methods=['GET', 'POST'])  
# def update_order(id):
#     all_orders = order_form.query.all()
#     my_order_update= my_order
#     db.session.commit()


#     #This route allows for a form to be filled in again to change the order
#     #only the product changes in this case
   


# @app.route('/delete/<id>', methods=['GET', 'POST']) 
# delete_order(id_num):
#         all_orders = order_form.query.all()
#         my_order_delete= all_orders.query.get(id_num)
#         db.session.delete(my_order_delete)
#         db.session.commit()
#  #redirect to shop URL
#  #doesnt need a render template
#  #query database and delete object then return to @route shop


#     def update(id_num):
#         all_orders = order_form.query.all()
#         my_order_update= my_order
#         db.session.commit()
#         return my_order_update

#     def delete_order(id_num):
#         all_orders = order_form.query.all()
#         my_order_delete= all_orders.query.get(id_num)
#         db.session.delete(my_order_delete)
#         db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)