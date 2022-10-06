from flask import Flask, render_template,redirect,flash,url_for
#Importamos la clase de nuestro formulario
from forms import FromInicio
import registroUsuario as formu
import asigVueloPiloto as formuAsigPiloto
import listVueloCliente as formuVueloCliente
#impotamos el servicio de nuestro sistema operativo para
#que nos genere el token
import os
app = Flask(__name__)
#codigo que genera nuestro token
app.secret_key = os.urandom(24)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET","POST"])
def login():
    #instacio la clase de mi formulario
    formularioLogin = FromInicio()
    if(formularioLogin.validate_on_submit()):
        flash("Inicio de sesion del usuario {} y solicito {}".format(formularioLogin.usuario.data, formularioLogin.recordar.data))
        return redirect(url_for("gracias"))
    return render_template("inicioSesion.html", formularioLoginVista = formularioLogin)

@app.route("/gracias")
def gracias():
    return render_template("gracias.html")

@app.route("/registrarusuario")
def registarusuario():
    formRegisUsu = formu.FromRegisUsuario()
    return render_template('registroUsuario.html', formRegisUsuVista = formRegisUsu)

@app.route("/asigvuelopiloto")
def asigVueloPiloto():
    formAsigVueloPilo = formuAsigPiloto.vueloPiloto()
    return render_template('regisVuelosPilotos.html', formAsigVueloPilotoVista = formAsigVueloPilo)

@app.route("/vuelosclientes")
def asigVueloCliente():
    formAsigVueloCliente = formuVueloCliente.vuelosCliente()
    return render_template('vuelosCliente.html', formAsigVueloClienteVista = formAsigVueloCliente)


app.run(debug=True)