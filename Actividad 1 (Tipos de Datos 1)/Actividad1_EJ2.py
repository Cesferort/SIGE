# -*- coding: utf-8 -*-
class Actividad1_EJ2:
    def main(self):
        nombre = "César"
        apellido = "Ferreiro Ortiz de Guinea"
        localidad = "Vitoria-Gasteiz"
        resultado = "Yo soy " + nombre + " " + apellido + " y vivo en " +  localidad

        print(resultado)
        print("Lo escrito tiene " + str(resultado.__len__()) + " carácteres\n\n")

        resultado = "Yo soy {} {} y vivo en {}"
        print(resultado.format(nombre, apellido, localidad))

        print("\t\t\t\t\t" + resultado.format(apellido, apellido, localidad).upper())

ej2 = Actividad1_EJ2()
ej2.main()