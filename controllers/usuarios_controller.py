from flask import render_template, request
from flask_controller import FlaskController 
from src.models.usuarios import Usuarios
from src.app import app

class UsuariosController(FlaskController):   
    @app.route ('/lista_usuarios')
    def lista_usuarios():
        try:
            usuarios = Usuarios.traer_usuarios()
            return render_template('lista_usuarios.html',titulo='Lista usuarios', usuarios = usuarios)
        except:
            return render_template('lista_clientes.html',titulo='Error de conexión a la base de datos')
        
    @app.route ('/formulario_usuarios', methods=['GET','POST'])
    def formulario_usuarios_html():
        if request.method == 'POST':
            nombres = request.form.get('nombres')
            apellidos = request.form.get('apellidos')
            email = request.form.get('email')
            direccion = request.form.get('direccion')
            telefono = request.form.get('telefono')
            puesto = request.form.get('puesto')
            documento_identidad = request.form.get('documento_identidad')
            contraseña = request.form.get('contraseña')
            usuario_almacenar = Usuarios(nombres,apellidos,email,direccion,telefono,puesto,documento_identidad,contraseña)
            usuario_repetido =  Usuarios.traer_usuario_por_documento_identidad(documento_identidad)
            if usuario_repetido:
                return render_template('formulario_usuarios.html'
                                    ,titulo='Crear Usuario'
                                    ,errorUsuario = 'El documento de identidad no se puede repetir'
                                    ,usuario_almacenar = usuario_almacenar)
            try:
                Usuarios.crear_usuario(usuario_almacenar)
            except:            
                return render_template('formulario_usuarios.html',titulo='Error al registrar en la base de datos')    
        return render_template('formulario_usuarios.html', titulo='Crear Usuario')
