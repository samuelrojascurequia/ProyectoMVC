from flask import render_template, request
from flask_controller import FlaskController
from src.models.clientes import Clientes
from src.app import app

class ClientesController(FlaskController):
    @app.route('/lista_clientes')
    def lista_clientes():
        try:
            clientes = Clientes.traer_clientes()
            return render_template('lista_clientes.html',titulo='Lista clientes', clientes = clientes)
        except:
            return render_template('lista_clientes.html',titulo='Error de conexión a la base de datos')
    
    @app.route ('/formulario_clientes', methods=['GET','POST'])
    def formulario_clientes_html():
        if request.method == 'POST':
            nombres = request.form.get('nombres')
            apellidos = request.form.get('apellidos')
            email = request.form.get('email')
            ciudad = request.form.get('ciudad')
            departamneto = request.form.get('departamento')
            direccion = request.form.get('direccion')
            documento_identidad = request.form.get('documento_identidad')
            telefono = request.form.get('telefono')
            cliente_almacenar = Clientes(nombres,apellidos,email,ciudad,departamneto,direccion,documento_identidad,telefono)
            cliente_repetido =  Clientes.traer_cliente_por_documento_identidad(documento_identidad)
            if cliente_repetido:
                return render_template('formulario_clientes.html'
                                    ,titulo='Crear Cliente'
                                    ,errorCliente = 'El documento de identificacion no se puede repetir'
                                    ,cliente_almacenar = cliente_almacenar)
            try:
                Clientes.crear_cliente(cliente_almacenar)
            except:            
                return render_template('formulario_clientes.html',titulo='Error al registrar en la base de datos')    
        return render_template('formulario_clientes.html', titulo='Crear Cliente')

  