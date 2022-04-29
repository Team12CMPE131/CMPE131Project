from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, Email, EqualTo, DataRequired

class register(FlaskForm):
    username = StringField(label='Username: ', validators=[Length(min=2, max =32), DataRequired()])
    email_address = StringField(label='Email: ',validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password: ', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm password: ', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label = 'Create Account') 
