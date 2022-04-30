from wtforms import validators, Form, StringField, DecimalField, FileField, RadioField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import Length, Email, EqualTo, DataRequired

class ListItemForm(Form):
    item_name = StringField('Item Name', [validators.DataRequired(), validators.Length(max = 20)])
    item_price = DecimalField('Item Price', [validators.DataRequired()])
    item_description = StringField('Item Description', [validators.DataRequired(), validators.Length(max = 280)])
    item_picture = FileField('Item Picture', [validators.DataRequired()])
    auction_choice = RadioField('Auction?', [validators.DataRequired()], choices=['Auction', 'List'])

class register(FlaskForm):
    username = StringField(label='Username: ', validators=[Length(min=2, max =32), DataRequired()])
    email_address = StringField(label='Email: ',validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password: ', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm password: ', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label = 'Create Account') 
