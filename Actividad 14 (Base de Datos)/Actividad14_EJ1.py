# -*- coding: utf-8 -*-
import sqlite3
class Actividad14_EJ1:
    def main(self):
        # Preparar tabla
        self.conexBBDD()
        self.vaciarBBDD()
        self.crearBBDD()
        self.con.commit()

        # Rellenar tabla
        productos = \
            {
                1 : (1, "Lapicero", "Útil de escritura", 1),
                2: (2, "Ratón inalámbrico", "Óptico Wireless", 14.2),
                3: (3, "Chinchetas", "Caja de 100 unidades", 9.93),
                4: (4, "Soldador", "Pack soldador estaño y flux", 25.67)
            }
        query = "INSERT INTO `productos` (`id_product`, `nombre`, `descripcion`, `precio`) VALUES"
        query += " (" + self.comodin + ", " + self.comodin + ", " + self.comodin + ", "+ self.comodin + ");"
        self.cursor.executemany(query, productos.values())

        # Actualizar tabla
        query = "UPDATE productos "
        query += "SET precio = 29.99 "
        query += "WHERE " + self.comodin + " = nombre;"
        self.cursor.execute(query, ("Soldador",))

        # Visualizar tabla
        self.visualizarTabla()

        # Eliminar lapicero
        query = "DELETE FROM productos "
        query += "WHERE nombre = " + self.comodin + ";"
        self.cursor.execute(query, ("Lapicero",))

        # Visualizar tabla tras la eliminación del lapicero
        print("\nLapicero eliminado")
        self.visualizarTabla()

        # Cierre del conector y del cursor
        self.con.commit()
        self.cursor.close()
        self.con.close()

    def conexBBDD(self):
        self.con = sqlite3.connect("bbdd.db")
        self.cursor = self.con.cursor()
        self.comodin = "?"

    def vaciarBBDD(self):
        self.cursor.execute("DROP TABLE IF EXISTS productos")

    def crearBBDD(self):
        self.cursor.execute("DROP TABLE IF EXISTS productos")
        with open('bbdd-lite.sql', 'r') as fSQL:
            fSQLString = fSQL.read()
            self.cursor.executescript(fSQLString)

    def visualizarTabla(self):
        query = "SELECT      id_product, nombre, descripcion, precio "
        query += "FROM        productos "
        query += "ORDER BY    id_product;"
        self.cursor.execute(query)
        cont = 1
        for row in self.cursor:
            print("\nProducto " + str(cont) + ":\n\tCódigo\t\t\t\t\tNombre\t\t\t\t\tDescripcion\t\t\t\t\tPrecio")
            print("\t" + str(row[0]) + "\t\t\t\t\t" + str(row[1]) + "\t\t\t\t\t" + str(row[2]) + "\t\t\t\t\t" + str(
                row[3]))
            cont = cont + 1
        print()

ej1 = Actividad14_EJ1()
ej1.main()