# -*- coding: utf-8 -*-
class Actividad4_EJ1:
    def main(self):
        datosIncorrectos = True
        while datosIncorrectos == True:
            try:
                inicial = int(input("Inicial:"))
                final = int(input("Final:"))
                incDec = int(input("Incremento/Decremento:"))
                datosIncorrectos = False
            except:
                print("Dato no permitido.\nVuelve a intentarlo\n")

        i = inicial
        max = final
        resultado = ""
        while i <= max:
            resultado += (str(i) + "\t")
            i += incDec
        print(resultado)

ej1 = Actividad4_EJ1()
ej1.main()