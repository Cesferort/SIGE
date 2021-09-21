# -*- coding: utf-8 -*-
class Actividad3_EJ3:
    def main(self):
        self.funcion(-6)
        self.funcion(1.23)

    def funcion(self, x):
        resultado = 0
        if x < 0:
            resultado = (x * x) - x
        else:
            resultado = (-x * x) + 3 * x
        print("Función a calcular:\nf( " + str(x) + " ) = " + str(resultado) + "\n")

ej3 = Actividad3_EJ3()
ej3.main()