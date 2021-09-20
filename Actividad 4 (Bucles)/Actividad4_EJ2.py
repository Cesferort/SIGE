# -*- coding: utf-8 -*-
class Actividad4_EJ2:
    def main(self):
        datoIncorrecto = True
        while datoIncorrecto == True:
            try:
                n = int(input("Dime cuántos números vas a escribir: "))
                datoIncorrecto = False
            except:
                print("Dato no permitido.\nVuelve a intentarlo\n")

        sumaTotal = 0
        i = 0
        max = n
        while i < max:
            datoIncorrecto = True
            while datoIncorrecto == True:
                try:
                    n = int(input("Dame el número " + str(i+1) + ": "))
                    sumaTotal += n
                    i += 1
                    datoIncorrecto = False
                except:
                    print("Dato no permitido.\nVuelve a intentarlo\n")
            print(i)
        print("La suma de los números que has escrito es: " + str(sumaTotal))

ej2 = Actividad4_EJ2()
ej2.main()