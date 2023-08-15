import sqlite3

class Producto:
    def setID(self, id):
        self.ID = id
    def setNombre(self, nombre):
        self.Nombre = nombre
    def setCosto(self, costo):
        self.Costo = costo
    def setPrecio(self, precio):
        self.Precio = precio
    def getID(self):
        return self.ID
    def getNombre(self):
        return self.Nombre
    def getCosto(self):
        return self.Costo
    def getPrecio(self):
        return self.Precio

class ProductoDAO:
    def createProducto(self, producto):
        sql = '''INSERT INTO Producto(nombreProducto,costoUnitario,precioUnitario) VALUES(?,?,?)'''
        conn = sqlite3.connect("inventarios.db")
        conn.execute(sql,(producto.getNombre(),producto.getCosto(),producto.getPrecio()))
        conn.commit()
        conn.close()
    def selectOne(self, producto):
        sql = '''SELECT * FROM Producto WHERE idProducto=?'''
        conn = sqlite3.connect("inventarios.db")
        cursor = conn.execute(sql,(producto.getID(),))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row
    def selectAll(self):
        sql = '''SELECT * FROM Producto'''
        conn = sqlite3.connect("inventarios.db")
        cursor = conn.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    def selectIDfromName(self,nombreProducto):
        sql = '''SELECT * FROM Producto WHERE nombreProducto=?'''
        conn = sqlite3.connect("inventarios.db")
        cursor = conn.execute(sql,(nombreProducto,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row[0]