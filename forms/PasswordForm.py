from flask_wtf import  FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import PasswordInput

class PasswordForm(FlaskForm):
    password = StringField('New password', validators=[DataRequired()], widget=PasswordInput(hide_value=False))
    repeat_password = StringField('Repeat password', validators=[DataRequired()], widget=PasswordInput(hide_value=False))
    submit = SubmitField('Submit')