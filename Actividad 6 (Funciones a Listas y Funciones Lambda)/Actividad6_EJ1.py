# -*- coding: utf-8 -*-
class Actividad6_EJ1:
    def main(self):
        datoIncorrecto = True
        while datoIncorrecto == True:
            try:
                n = int(input("Dime cuántos números vas a escribir: "))
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
                    n = int(input("Dame el número " + str(i + 1) + ": "))
                    listaN.append(n)
                    i += 1
                    datoIncorrecto = False
                except:
                    print("Dato no permitido.\nVuelve a intentarlo\n")
        print(str(self.conseguirPares(listaN)))

    def conseguirPares(self, listaN):
        resultado = []
        for n in listaN:
            if n % 2 == 0:
                resultado.append(n)
        return resultado

ej1 = Actividad6_EJ1()
ej1.main()