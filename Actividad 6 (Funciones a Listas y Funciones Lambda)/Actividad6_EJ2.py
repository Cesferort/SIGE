# -*- coding: utf-8 -*-
class Actividad6_EJ2:
    def main(self):
        r1 = float(input("R1:"))
        r2 = float(input("R2:"))
        r3 = float(input("R3:"))
        print(str(self.ecuacion(r1, r2, r3)))

    def ecuacion(self, r1, r2, r3):
        return (1 / (1 / r1 + 1 / r2 + 1 / r3))

ej2 = Actividad6_EJ2()
ej2.main()