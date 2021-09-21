# -*- coding: utf-8 -*-
class Actividad3_EJ1:
    def main(self):
        self.pruebas(2, 2, 4)
        self.pruebas(1, 2, 4)
        self.pruebas(1, 2, 2)
        self.pruebas(2, 2, 2)

    def pruebas(self, a, b, c):
        print("Lados del triángulo " + str(a) + " " + str(b) + " " + str(c))
        if a == b and a == c:
            print("Triángulo Equilátero")
        elif a == b or b == c:
            print("Triángulo Isósceles")
        else:
            print("Triángulo Escaleno")
        print()

ej1 = Actividad3_EJ1()
ej1.main()