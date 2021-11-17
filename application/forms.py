from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField 
from wtforms.validators import DataRequired, ValidationError


from application.models import orders, products

class trolley_check:
    def __init__(self,message):
        self.message = message

    def __call__(self, form, field):
        all_series = trolley.query.all()
        for trolley in all_trolley:
            if series.name == field.data:
                raise ValidationError(self.message)
    
class trolley_form(FlaskForm):
    name = StringField('Trolley name', 
		validators=[
			DataRequired(),
			SeriesCheck(message='This trolley name already exists')])
    submit = SubmitField('Create Trolley')

class products_form(FlaskForm):
    desc = StringField('Product',
		validators=[
			DataRequired()])
    rating = SelectField('Ratings',
		choices=[
			('5', '5/5'),('4','4/5'),('3','3/5'),('2','2/5'),('1','1/5'), ('0','0/5')])
    submit = SubmitField('Add Review')


    



