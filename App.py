from flask import *
import sqlite3
from models.Producto import ProductoDAO, Producto
from models.Entrada import EntradaDAO, Entrada
from models.Salida import SalidaDAO, Salida

app = Flask(__name__)

app.secret_key = 'mykey'

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/productos')
def list_products():
    dao = ProductoDAO()
    rows = dao.selectAll()
    return render_template("productos.html", productos = rows)

@app.route('/addProducto', methods=['POST'])
def add_Producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        costo = request.form['costo']
        precio = request.form['precio']
        producto = Producto()
        producto.setNombre(nombre)
        producto.setCosto(float(costo))
        producto.setPrecio(float(precio))
        dao = ProductoDAO()
        dao.createProducto(producto)
        flash("Producto Añadido Correctamente")
        return redirect(url_for('list_products'))

@app.route('/entradas')
def list_entradas():
    dao1 = EntradaDAO()
    dao2 = ProductoDAO()
    rows = dao1.selectAll()
    filas = []
    for row in rows:
        producto = Producto()
        producto.setID(row[3])
        filas.append((row[0],row[1],row[2],dao2.selectOne(producto)[1]))
    return render_template("entradas.html", entradas = filas, productos = dao2.selectAll())

@app.route('/addEntrada', methods=['POST'])
def add_Entrada():
    if request.method == 'POST':
        fecha = request.form['fecha']
        cantidad = request.form['cantidad']
        idProducto = request.form['producto']
        entrada = Entrada()
        entrada.setFecha(fecha)
        entrada.setCantidad(int(cantidad))
        entrada.setIdProducto(int(idProducto))
        dao = EntradaDAO()
        dao.createEntrada(entrada)
        flash("Entrada registrada correctamente")
        return redirect(url_for('list_entradas'))

@app.route('/salidas')
def list_salidas():
    dao1 = SalidaDAO()
    dao2 = ProductoDAO()
    rows = dao1.selectAll()
    filas = []
    for row in rows:
        producto = Producto()
        producto.setID(row[5])
        filas.append((row[0],row[1],row[2],row[3],row[4],dao2.selectOne(producto)[1]))
    return render_template("salidas.html", salidas = filas, productos = dao2.selectAll())

@app.route('/addSalida', methods=['POST'])
def add_Salida():
    if request.method == 'POST':
        fecha = request.form['fecha']
        cantidad = request.form['cantidad']
        cantidad = int(cantidad)
        idProducto = request.form['producto']
        idProducto = int(idProducto)
        daoP = ProductoDAO()
        producto = Producto()
        producto.setID(idProducto)
        if getInventarioActual(daoP.selectOne(producto)) < cantidad:
            flash("No hay suficiente mercancia para la salida")
            flash("danger")
            return redirect(url_for('list_salidas'))
        costoP = daoP.selectOne(producto)[2]
        precioP = daoP.selectOne(producto)[3]
        salida = Salida()
        salida.setFecha(fecha)
        salida.setCantidad(cantidad)
        salida.setCosto(costoP * cantidad)
        salida.setVenta(precioP * cantidad)
        salida.setIdProducto(idProducto)
        daoS = SalidaDAO()
        daoS.createSalida(salida)
        flash("Salida añadida correctamente")
        flash("success")
        return redirect(url_for('list_salidas'))

@app.route('/inventario')
def list_inventario():
    dao = ProductoDAO()
    listProductos = dao.selectAll()
    listInventario = []
    for producto in listProductos:
        listInventario.append((producto[0],producto[1],getInventarioActual(producto)))
    return render_template('inventario.html', inventario = listInventario)

def getInventarioActual(producto):
    conn = sqlite3.connect('inventarios.db')
    sqlEntradas = '''SELECT sum(cantidadEntrada) FROM Entrada WHERE idProducto =''' + str(producto[0])
    sqlSalidas = '''SELECT sum(cantidadSalida) FROM Salida WHERE idProducto =''' + str(producto[0])
    cursor = conn.execute(sqlEntradas)
    totalEntradas = cursor.fetchone()[0]
    cursor = conn.execute(sqlSalidas)
    totalSalidas = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return totalEntradas - totalSalidas

if __name__ == "__main__":
    app.run(port=3000, debug=True)