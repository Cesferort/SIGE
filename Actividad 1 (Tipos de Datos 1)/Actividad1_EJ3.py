# -*- coding: utf-8 -*-
class Actividad1_EJ3:
    def main(self):
        cadenas = ["Amaia", "Marañon", "Vitoria-Gasteiz"]
        print("Arrays de cadenas EJ3")

        #EJ1
        resultado = ""
        for cadena in cadenas:
            resultado += cadena + "#"
        print("Ejem1: " + resultado)

        # EJ2
        resultado = ""
        for cadena in cadenas:
            resultado += cadena + "--"
        print("Ejem2: " + resultado)

        # EJ3
        resultado = ""
        esPrimeraVez = True
        for cadena in cadenas:
            if esPrimeraVez == True:
                esPrimeraVez = False
                resultado += cadena
            else:
                resultado += "\n" + cadena
        print("Ejem3: " + resultado)

        # EJ4
        resultado = ""
        for cadena in cadenas:
            resultado += cadena + "\t\t\t"
        print("Ejem4: " + resultado)

        # EJ5
        resultado = ""
        for cadena in cadenas:
            resultado += cadena + " "
        print("Ejem5: " + resultado)

ej3 = Actividad1_EJ3()
ej3.main()