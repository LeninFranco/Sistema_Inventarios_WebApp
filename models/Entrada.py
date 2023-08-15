import sqlite3

class Entrada:
    def setID(self,id):
        self.ID = id
    def setFecha(self,fecha):
        self.Fecha = fecha
    def setCantidad(self,cantidad):
        self.Cantidad = cantidad
    def setIdProducto(self,idproducto):
        self.IdProducto = idproducto
    def getID(self):
        return self.ID
    def getFecha(self):
        return self.Fecha
    def getCantidad(self):
        return self.Cantidad
    def getIdProducto(self):
        return self.IdProducto

class EntradaDAO:
    def createEntrada(self,entrada):
        sql = '''INSERT INTO Entrada(fechaEntrada,cantidadEntrada,idProducto) VALUES(?,?,?)'''
        conn = sqlite3.connect("inventarios.db")
        conn.execute(sql,(entrada.getFecha(),entrada.getCantidad(),entrada.getIdProducto()))
        conn.commit()
        conn.close()
    def selectOne(self,entrada):
        sql = '''SELECT * FROM Entrada WHERE idEntrada=?'''
        conn = sqlite3.connect("inventarios.db")
        cursor = conn.execute(sql,(entrada.getID(),))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row
    def selectAll(self):
        sql = '''SELECT * FROM Entrada'''
        conn = sqlite3.connect("inventarios.db")
        cursor = conn.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

if __name__ == "__main__":
    dao = EntradaDAO()
    print(dao.selectAll())