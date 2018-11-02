from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,SelectField
from wtforms.validators import DataRequired

class http_req_forms(FlaskForm):
    c_s = SelectField('Create Session?', choices = [('NO','NO'),('YES','YES')])
    req = SelectField('Select Request type:', choices = [('POST','POST'),('GET','GET'),('PUT','PUT'),('DELETE','DELETE'),('HEAD','HEAD'),('OPTIONS','OPTIONS')])    
    url = StringField('Insert URL:' ,validators = [DataRequired()])
    c_ua = SelectField('Change User Agent?', choices = [('NO','NO'),('YES','YES')])
    in_ua = StringField('Insert User Agent:')
    execute = SubmitField('Execute')

class href_finder(FlaskForm):
    url = StringField('Insert URL:' ,validators = [DataRequired()])
    execute = SubmitField('Execute')
