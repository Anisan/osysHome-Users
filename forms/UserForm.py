from flask_wtf import  FlaskForm
from wtforms import StringField, SubmitField, SelectField 
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    image = StringField('Image')
    role = SelectField('Role',choices=(("user","User"),("guest","Guest"), ("editor","Editor"), ("admin","Administrator")), validators=[DataRequired()])
    home_page = StringField('Home page')
    apikey = StringField('API key')
    timezone = StringField('Timezone')
    submit = SubmitField('Submit')
