from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateTimeField
from wtforms.validators import InputRequired, ValidationError

from application.models import orders, product 

# class order_check: 
#     def validate_name(form, field):
#         if len(field.data) > 50:
#             raise ValidationError('Name must be less than 50 characters')
    
class order_form(FlaskForm):

    first_name = StringField('First name')

    last_name = StringField('Last name')

    email = StringField('Email name')

    product = SelectField(
        choices = [('Chicken, ', 'Lamb', 'Cow', 'Fish', 'Sheep'])

    #do the tuple method (chkn, chicken)

    collection = StringField('Chosen Date and time of Colelction')

    submit = SubmitField('Place Order')



