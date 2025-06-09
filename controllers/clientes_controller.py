from flask import render_template, request
from flask_controller import FlaskController 
from src.app import app

class ClientesController():    
    @app.route ('/clientes')
    def clientes_html():
        return render_template('clientes.html', titulo='Lista Clientes')

    @app.route ('/formulario_clientes')
    def formulario_clientes_html():
        return render_template('formulario_clientes.html', titulo='Crear Cliente')

