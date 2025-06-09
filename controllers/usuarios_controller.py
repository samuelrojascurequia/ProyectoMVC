from flask import render_template, request
from flask_controller import FlaskController 
from src.models.productos import Productos
from src.models.categorias import Categorias
from src.app import app

class UsuariosController(FlaskController):   
    @app.route ('/usuarios')
    def usuarios_html():
        return render_template('usuarios.html', titulo='Lista Usuario')

    @app.route ('/formulario_usuarios')
    def formulario_usuarios_html():
        return render_template('formulario_usuarios.html', titulo='Crear Usuario')

