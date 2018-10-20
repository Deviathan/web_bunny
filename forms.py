from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField
from wtforms.validators import DataRequired

class url_form(FlaskForm):
    url = StringField('URL' ,validators = [DataRequired()])
    c_ua = BooleanField("Want to change User-Agent?")
    execute = SubmitField('Execute') 