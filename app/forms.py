from flask import Flask
from wtforms.validators import Length, Email, EqualTo, DataRequired, ValidationError
from app.models import User
from wtforms import validators, StringField, DecimalField, FileField, RadioField, PasswordField, SubmitField, HiddenField
from flask_wtf import FlaskForm
from wtforms.validators import Length, Email, EqualTo, DataRequired, NumberRange

class ListItemForm(FlaskForm):
    item_name = StringField('Enter Item Name', [validators.DataRequired(), validators.Length(max = 20)])
    item_price = DecimalField('Enter Item Price', [validators.DataRequired()])
    item_description = StringField('Enter Item Description', [validators.DataRequired(), validators.Length(max = 280)])
    item_picture = FileField('Upload Item Picture')
    auction_choice = RadioField('Auction?', [validators.DataRequired()], choices=['Auction', 'Sale'])
    auction_length = DecimalField('Length of Auction', 
                                  validators=[NumberRange(0, 59, 'Must be a value between 0 and 59')])
    submit = SubmitField('List Item on Market!')

class register(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username = username_to_check.data).first()
        if user:
            raise ValidationError('Username already exist!Please try something else')

    def validate_email_address(self, email_address_to_check):
        email = User.query.filter_by(email_address = email_address_to_check.data).first()
        if email:
            raise ValidationError('Email address already exist!Please try something else')
         

    username = StringField(label='Username: ', validators=[Length(min=2, max =32), DataRequired()])
    email_address = StringField(label='Email: ',validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password: ', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm password: ', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label = 'Create Account') 

class LoginForm(FlaskForm):
    username = StringField(label='Username:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Login')

class SearchForm(FlaskForm):
    name = StringField(label='What are you looking for?', validators=[DataRequired()])

class purchaseItemForm(FlaskForm):
    submit = SubmitField(label='Buy item')
    
class addToCart(FlaskForm):
    submit = SubmitField(label="Add to Cart")

class deleteUser(FlaskForm):
    submit = SubmitField(label="Delete User")
    
class CompareItemButton(FlaskForm):
    item_id = HiddenField(validators=[DataRequired()])
    second_id = HiddenField()
    submit = SubmitField(label='Compare Items...')
    
class BidButton(FlaskForm):
    item_id = HiddenField(validators=[DataRequired()])
    price = DecimalField(validators=[DataRequired()])
    submit = SubmitField(label='Confirm Bid')
