# -*- coding: utf-8 -*-
class Actividad4_EJ3:
    def main(self):
        self.__password__ = "kaixo1234"

        numIntento = 1
        maxIntentos = 3
        passwordAcertada = False
        while numIntento <= maxIntentos and passwordAcertada == False:
            inputUser = input("Introduzca la contraseña: ")
            if inputUser == self.__password__:
                passwordAcertada = True
            else:
                numIntento += 1

        if passwordAcertada == True:
            print("Bienvenido/a al sistema. Lo has conseguido en el intento número " + str(numIntento))
        else:
            print("Usuario/a bloqueado/a. Ponte en contacto con la persona administradora de la red.")

ej3 = Actividad4_EJ3()
ej3.main()