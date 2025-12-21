from flask_wtf import  FlaskForm
from wtforms import StringField, SubmitField, SelectField 
from wtforms.validators import DataRequired
from zoneinfo import available_timezones


def get_timezone_choices():
    """Возвращает отсортированный список часовых поясов для выпадающего списка"""
    timezones = sorted(available_timezones())
    return [(tz, tz) for tz in timezones]


class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    image = StringField('Image')
    role = SelectField('Role',choices=(("user","User"),("guest","Guest"), ("editor","Editor"), ("admin","Administrator")), validators=[DataRequired()])
    home_page = StringField('Home page')
    apikey = StringField('API key')
    timezone = SelectField('Timezone', choices=get_timezone_choices())
    submit = SubmitField('Submit')
