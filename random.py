# if len(first_name) == 0 or len(last_name) == 0:
#             error = 'Please supply both first and last name'
#         if len(email) == 0:
#             error = 'Please insert an email address so that we can update you regard your order'
#         if len(collection_date_time) == 0: 
#             error = 'Please state enter your preffered date and time for collection'
#         if #no selection for the product 


# product = SelectField(
    #     choices= [(1, 'Chicken') , (2,'Lamb'), (3, 'Cow'), (4,'Fish'), (5, 'Sheep')])

    # #     choices= ['Chicken','Lamb','Cow','Fish','Sheep'])

    # # choices= [(1, 'Chicken') , (2,'Lamb'), (3, 'Cow',) (4,'Fish'), (5, 'Sheep')])

    # #do the tuple method (chkn, chicken)


 # new_order = orders(first_name, last_name, email, product, collection_date_time)
        # ^why does this not work? 

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