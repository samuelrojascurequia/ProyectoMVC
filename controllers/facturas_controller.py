from flask import render_template, request
from flask_controller import FlaskController 
from src.app import app

class FacturasController():    
    @app.route ('/lista_facturas')
    def lista_facturas_html():
        return render_template('lista_facturas.html', titulo='Lista Facturas')

    @app.route ('/facturas')
    def facturas_html():
        return render_template('facturas.html', titulo='Crear Facturas')
