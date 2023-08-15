import sqlite3

class Salida:
    def setID(self,id):
        self.ID = id
    def setFecha(self,fecha):
        self.Fecha = fecha
    def setCantidad(self,cantidad):
        self.Cantidad = cantidad
    def setCosto(self,costo):
        self.Costo = costo
    def setVenta(self,venta):
        self.Venta = venta
    def setIdProducto(self,idproducto):
        self.IdProducto = idproducto
    def getID(self):
        return self.ID
    def getFecha(self):
        return self.Fecha
    def getCantidad(self):
        return self.Cantidad
    def getCosto(self):
        return self.Costo
    def getVenta(self):
        return self.Venta
    def getIdProducto(self):
        return self.IdProducto

class SalidaDAO:
    def createSalida(self,salida):
        sql = '''INSERT INTO Salida(fechaSalida,cantidadSalida,costoTotal,precioTotal,idProducto) VALUES(?,?,?,?,?)'''
        conn = sqlite3.connect("inventarios.db")
        conn.execute(sql,(salida.getFecha(),salida.getCantidad(),salida.getCosto(),salida.getVenta(),salida.getIdProducto()))
        conn.commit()
        conn.close()
    def selectOne(self,salida):
        sql = '''SELECT * FROM Salida WHERE idSalida=?'''
        conn = sqlite3.connect("inventarios.db")
        cursor = conn.execute(sql,(salida.getID(),))
        row = cursor.fetchone()
        return row
    def selectAll(self):
        sql = '''SELECT * FROM Salida'''
        conn = sqlite3.connect("inventarios.db")
        cursor = conn.execute(sql)
        rows = cursor.fetchall()
        return rows