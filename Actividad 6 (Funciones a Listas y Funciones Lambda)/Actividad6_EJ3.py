# -*- coding: utf-8 -*-
class Actividad6_EJ3:
    def main(self):
        datoIncorrecto = True
        while datoIncorrecto == True:
            try:
                n = int(input("Dime cuántas resistencias vas a conetar: "))
                datoIncorrecto = False
            except:
                print("Dato no permitido.\nVuelve a intentarlo\n")

        i = 0
        max = n
        listaN = []
        while i < max:
            datoIncorrecto = True
            while datoIncorrecto == True:
                try:
                    n = int(input("Dame la resistencia " + str(i + 1) + ": "))
                    listaN.append(n)
                    i += 1
                    datoIncorrecto = False
                except:
                    print("Dato no permitido.\nVuelve a intentarlo\n")
        print(str(self.ecuacion(listaN)))

    def ecuacion(self, listaN):
        divisor = 0
        for n in listaN:
            try:
                divisor += (1 / n)
            except:
                print("División entre 0 ignorada...")
        return 1 / divisor

ej3 = Actividad6_EJ3()
ej3.main()