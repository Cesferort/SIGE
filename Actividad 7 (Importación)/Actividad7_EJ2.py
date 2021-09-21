# -*- coding: utf-8 -*-
from datetime import date
import math
import os
class Actividad7_EJ2:
    def main(self):
        print(self.calcularEdad(1999, 6, 30))
        print(self.funcion(25))
        self.crearDirectorio()

    def calcularEdad(self, anio, mes, dia):
        ahora = date.today()
        fecha = date(anio, mes, dia)
        return ahora -fecha

    def funcion(self, n):
        return math.log(math.sqrt(n) * math.pi, 10)

    def crearDirectorio(self):
        try:
            ruta = "Importacion"
            os.makedirs(ruta)
            ruta += "/LibSistema"
            os.makedirs(ruta)
            print("Directorios creados correctamente.\n")
        except:
            print("Esta carpeta ya existe.\n")

ej2 = Actividad7_EJ2()
ej2.main()