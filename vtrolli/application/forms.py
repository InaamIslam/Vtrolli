from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField
from wtforms.validators import InputRequired, ValidationError

from application.models import orders, products

# class order_check: 
#     def validate_name(form, field):
#         if len(field.data) > 50:
#             raise ValidationError('Name must be less than 50 characters')
    
class order_form(FlaskForm):

    first_name = StringField('First name: ')

    last_name = StringField('Last name: ')

    email = StringField('Email: ')

    product = StringField( 'My chosen product is: ')

    collection_date_time = StringField('Please state your preferred date and time for collection: ')

    submit = SubmitField('PLACE ORDER')
    



