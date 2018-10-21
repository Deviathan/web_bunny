from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,SelectField
from wtforms.validators import DataRequired

class url_form(FlaskForm):
    req = SelectField('Select REQ type:', choices = [('POST','POST'),('GET','GET'),('PUT','PUT'),('DELETE','DELETE'),('HEAD','HEAD'),('OPTIONS','OPTIONS')])    
    url = StringField('URL' ,validators = [DataRequired()])
    c_ua = SelectField('Change User Agent?', choices = [('NO','NO'),('YES','YES')])
    in_ua = StringField('Insert User Agent?',validators = [DataRequired()])

    execute = SubmitField('Execute')
