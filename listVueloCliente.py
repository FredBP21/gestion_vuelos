from tkinter.tix import Tree
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, EmailField
#importar libreria validaciones
from wtforms.validators import DataRequired,Length

class vuelosCliente(FlaskForm):
    True