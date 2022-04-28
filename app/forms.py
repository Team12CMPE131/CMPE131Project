from wtforms import validators, Form, StringField, DecimalField, FileField, RadioField

class ListItemForm(Form):
    item_name = StringField('Item Name', [validators.DataRequired(), validators.Length(max = 20)])
    item_price = DecimalField('Item Price', [validators.DataRequired()])
    item_description = StringField('Item Description', [validators.DataRequired(), validators.Length(max = 280)])
    item_picture = FileField('Item Picture', [validators.DataRequired()])
    auction_choice = RadioField('Auction?', [validators.DataRequired()], choices=['Auction', 'List'])