from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, EmailField
#importar libreria validaciones
from wtforms.validators import DataRequired,Length

class vueloPiloto(FlaskForm):
    piloto= SelectField('Piloto',choices=[('1','Jaime Andres'),('2','Jairo'),('3','Freddy')],render_kw={'class':'btn btn-outline-secondary dropdown-toggle'})