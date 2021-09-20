# -*- coding: utf-8 -*-
class Actividad3_EJ2:
    def main(self):
        self.creadorFactura(333333)
        self.creadorFactura(800)
        self.creadorFactura(1800)

    def creadorFactura(self, consumo):
        precio = 0.9
        if consumo < 1000:
            precio = 1.2
        elif consumo <= 1850:
            precio = 1
        gastoTotal = precio * consumo

        print("\t\t\t\t---------- FACTURA ----------")
        print("Consumo: " + str(consumo) + " KW/h")
        print("Se aplica el precio: " + str(precio) + "€")
        print("\t\t\t\t-----------------------------")
        print("\t\t\t\t\tGASTO TOTAL: " + str(gastoTotal) + "€\n")

ej2 = Actividad3_EJ2()
ej2.main()