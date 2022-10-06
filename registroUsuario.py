from random import choices
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, EmailField
#importar libreria validaciones
#from wtforms.validators import DataRequired,Length

class FromRegisUsuario(FlaskForm):
    identicacion= IntegerField('Identificacion',render_kw={'class':'form-control'})
    nombre= StringField('Nombre',render_kw={'class':'form-control'})
    genero= StringField('Genero',render_kw={'class':'form-control'})
    roles= SelectField('Rol usuario',choices=[('1','Cliente'),('2','Piloto'),('3','Super Usuario')],render_kw={'class':'btn btn-outline-secondary dropdown-toggle'})
    correo=EmailField('Correo',render_kw={'class':'form-control'})
    clave=PasswordField('Contraseña',render_kw={'class':'form-control'})
    estado=BooleanField('Estado',render_kw={'class':'form-check-input mt-0'}) 
    crear = SubmitField("Crear usuario")
