from flask import Flask, render_template, request
from application import app
from application.forms import order_form
from application.models import orders

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/shop', methods=['GET', 'POST'])
def add():
    form = order_form()
    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        product = form.product.data
        collection_date_time = form.collection_date_time.data
        new_order = orders(
            first_name = form.first_name.data, 
            last_name = form.last_name.data, 
            email = form.email.data,
            product = form.product.data,
            collection_date_time = form.collection_date_time.data)
        db.session.add(new_order)
        db.session.commit()
        return redirect(url_for('checkout', confirmation_order = new_order)) 
    return render_template('shop.html', form=form)

@app.route('/checkout/<id>')
def confirm(id):   
    my_order = orders.query.filter_by(id=id).first()
    return render_template('checkout.html', myorder = my_order, form=form)
        

@app.route('/update/<id>', methods=['GET', 'POST'])  
def update(id):
    form = order_form
    order_update = order_form.query.get(id)
    if form.validate_on_submit():
        order_update.product = form.product.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('update.html', myorder = my_order, form=form)

@app.route('/delete/<id>')
def delete(id):
    order_delete = orders.query.get(id)
    db.session.delete(order_delete)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)