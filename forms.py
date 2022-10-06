from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, EmailField
#importar libreria validaciones
from wtforms.validators import DataRequired,Length

class FromInicio(FlaskForm):
    usuario  = StringField("Usuario", validators=[DataRequired(message="El campo es obligatorio"), Length(min=1,max=10,message="Numero de caracteres no validos")])
    clave = PasswordField("Contraseña", validators=[DataRequired(message="El campo es obligatorio")])
    recordar = BooleanField("Recordar Usuario")
    enviar = SubmitField("Iniciar Sesion")