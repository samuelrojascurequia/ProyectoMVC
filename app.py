from flask import Flask , render_template, request
from sqlalchemy import Column, Integer, String, Float, Numeric, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import pymysql

app = Flask(__name__) 

if __name__ == '__main__':
    app.run(debug=True)

engine = create_engine("mysql+pymysql://root@localhost/factura234?charset=utf8mb4") 

connection = engine.connect()

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()

Base.metadata.bind = engine

@app.route ('/')
def index():
    return render_template('index.html', titulo='Bienvenido a Supermercados RC')

@app.route ('/facturas')
def facturas_html():
    return render_template('facturas.html', titulo='Crear Facturas')

@app.route ('/formulario_clientes')
def formulario_clientes_html():
    return render_template('formulario_clientes.html', titulo='Crear Cliente')

@app.route ('/formulario_producto', methods=['GET','POST'])
def formulario_producto_html():
    categorias = Categorias.traer_categorias() 
    if request.method == 'POST':
        codigo = request.form.get('codigo')
        descripcion = request.form.get('descripcion')
        unidad_medida = request.form.get('unidad_medida')
        cantidad_inventario = request.form.get('cantidad_inventario')
        precio_unitario = request.form.get('precio_unitario')
        categoria = request.form.get('categoria')
        producto_almacenar = Productos(codigo,descripcion,unidad_medida,cantidad_inventario,precio_unitario,categoria)
        producto_repetido =  session.query(Productos).filter(Productos.descripcion == descripcion).first()
        if producto_repetido:
            return render_template('formulario_producto.html'
                                   ,titulo='Crear Producto'
                                   ,errorProducto = 'La descripcion no se puede repetir'
                                   ,categorias = categorias
                                   ,producto_almacenar = producto_almacenar)
        try:
            Productos.crear_producto(producto_almacenar)
        except:            
            return render_template('formulario_producto.html',titulo='Error al registrar en la base de datos',categorias = categorias)    
    return render_template('formulario_producto.html', titulo='Crear Producto',categorias = categorias)

@app.route ('/formulario_usuarios')
def formulario_usuarios_html():
    return render_template('formulario_usuarios.html', titulo='Crear Usuario')

@app.route ('/lista_facturas')
def lista_facturas_html():
    return render_template('lista_facturas.html', titulo='Lista Facturas')

@app.route ('/lista_productos')
def lista_productos_html():
    try:
        productos = Productos.traer_productos()
        return render_template('lista_productos.html', titulo='lista Productos', productos = productos)
    except:
        return render_template('lista_productos.html', titulo='Error de conexion a la base de datos')
   
@app.route ('/login')
def login_html():
    return render_template('login.html')

@app.route ('/usuarios')
def usuarios_html():
    return render_template('usuarios.html', titulo='Lista Usuario')

@app.route ('/clientes')
def clientes_html():
    return render_template('clientes.html', titulo='Lista Clientes')

@app.route ('/se_guardo')
def se_guardo():
    return render_template('se_guardo.html')

class Productos(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    codigo = Column(String(9), unique=True, nullable=False)
    descripcion = Column(String(300), unique=True)
    unidad_medida = Column(String(3), nullable=False)
    cantidad_inventario = Column(Numeric(10,2), nullable=False)
    precio_unitario = Column(Numeric(10,2), nullable=False)
    categoria = Column(Integer, ForeignKey('categorias.id'), nullable=False)

    def __init__(self, codigo, descripcion, unidad_medida, cantidad_inventario, precio_unitario, categoria):
        self.codigo = codigo
        self.descripcion = descripcion
        self.unidad_medida = unidad_medida
        self.cantidad_inventario = cantidad_inventario
        self.precio_unitario = precio_unitario
        self.categoria = categoria
   
    def crear_producto(producto):
        producto = session.add(producto)
        session.commit()
        return producto
    
    def traer_productos():
       productos = session.query(Productos).all()
       return productos 
    
    


class Categorias(Base):
    __tablename__ = 'categorias'
    id = Column(Integer, primary_key=True)
    nombre_categoria = Column(String(300), unique=True, nullable=False)

    def __init__(self, nombre_categoria):
        self.nombre_categoria = nombre_categoria

    def traer_categorias():
        categorias = session.query(Categorias).all()
        return categorias


Base.metadata.create_all(engine)






    