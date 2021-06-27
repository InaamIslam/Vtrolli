from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField 
from wtforms.validators import DataRequired, ValidationError


from application.models import orders, products

    
class order_form(FlaskForm):
    first_name = StringField('First name:', validators = [DataRequired(),
        ] )

    last_name = StringField('Last name:', validators = [DataRequired(),
        ] )

    email = StringField('Email:', validators = [DataRequired(),
        ] )

    product = StringField( 'My chosen product is:', validators = [DataRequired(),
        ] )

    collection_date_time = StringField('Please state your preferred date and time for collection:', validators = [DataRequired(),
        ] )

    submit = SubmitField('PLACE ORDER')


    



