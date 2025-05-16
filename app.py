from flask import Flask , render_template, url_for

app = Flask(__name__) 

if __name__ == '__main__':
    app.run(debug=True)

@app.route ('/')
def index():
    return render_template('index.html', titulo='Bienvenido a Supermercados RC')

@app.route ('/facturas.html')
def facturas_html():
    return render_template('facturas.html', titulo='Crear Facturas')

@app.route ('/formulario_clientes.html')
def formulario_clientes_html():
    return render_template('formulario_clientes.html', titulo='Crear Cliente')

@app.route ('/formulario_producto.html')
def formulario_producto_html():
    return render_template('formulario_producto.html', titulo='Crear Producto')

@app.route ('/formulario_usuarios.html')
def formulario_usuarios_html():
    return render_template('formulario_usuarios.html', titulo='Crear Usuario')

@app.route ('/lista_facturas.html')
def lista_facturas_html():
    return render_template('lista_facturas.html', titulo='Lista Facturas')

@app.route ('/lista_productos.html')
def lista_productos_html():
    return render_template('lista_productos.html', titulo='lista Productos')

@app.route ('/login.html')
def login_html():
    return render_template('login.html')

@app.route ('/usuarios.html')
def usuarios_html():
    return render_template('usuarios.html', titulo='Lista Usuario')

@app.route ('/clientes.html')
def clientes_html():
    return render_template('clientes.html', titulo='Lista Clientes')

@app.route ('/se_guardo')
def se_guardo():
    return render_template('se_guardo.html')




    