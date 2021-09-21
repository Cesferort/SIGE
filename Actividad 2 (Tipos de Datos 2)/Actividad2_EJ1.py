# -*- coding: utf-8 -*-
class Actividad2_EJ1:
    def main(self):
        dicAsignaturas = \
        {
            "SIGE":"Sistemas de Gestión Empresarial",
            "PROM":"Programación multimedia",
            "PROS":"Programación servicios y procesos",
            "ADAT":"Acceso a datos"
        }
        print("ASIGNATURAS:")
        print(dicAsignaturas)

        dicAsignaturas["DEIN"] = "Diseño de interfaces"
        print("\nAÑADIR ASIGNATURA DEIN")
        print("ASIGNATURAS TRAS AÑADIR:")
        print(dicAsignaturas)

        print("\nValor de SIGE: " + dicAsignaturas.get("SIGE"))

        print("\nLISTADOS")
        listaClaves = "["
        esPrimeraVez = True
        for key in dicAsignaturas:
            if esPrimeraVez == True:
                esPrimeraVez = False
            else:
                listaClaves += ", "
            listaClaves += "´" + key + "´"
        listaClaves += "]"
        print("Lista de las claves: " + listaClaves)

        listaValores = "["
        esPrimeraVez = True
        for key in dicAsignaturas:
            if esPrimeraVez == True:
                esPrimeraVez = False
            else:
                listaValores += ", "
            listaValores += "´" + dicAsignaturas.get(key) + "´"
        listaValores += "]"
        print("Lista de los valores: " + listaValores)

        print("\nEXISTE???")
        check = True
        if dicAsignaturas.get("1") == None:
            check = False
        print("Existe la clave 1? " + str(check))
        check = True
        if dicAsignaturas.get("ADAT") == None:
            check = False
        print("Existe la clave ADAT? " + str(check))

        print("\nEliminar SIGE")
        del dicAsignaturas["SIGE"]
        listaClaves = "["
        esPrimeraVez = True
        for key in dicAsignaturas:
            if esPrimeraVez == True:
                esPrimeraVez = False
            else:
                listaClaves += ", "
            listaClaves += "´" + key + "´"
        listaClaves += "]"
        print("Claves tras eliminar SIGE: " + listaClaves)

        print("\nBuscar una función que elimine DEIN y nos devuelva su valor:")
        check = True
        if dicAsignaturas.get("DEIN") == None:
            check = False
        if check == True:
            print(dicAsignaturas.get("DEIN"))
            del dicAsignaturas["DEIN"]

        listaClaves = "["
        esPrimeraVez = True
        for key in dicAsignaturas:
            if esPrimeraVez == True:
                esPrimeraVez = False
            else:
                listaClaves += ", "
            listaClaves += "´" + key + "´"
        listaClaves += "]"
        print("Claves tras eliminar DEIN: " + listaClaves)

ej1 = Actividad2_EJ1()
ej1.main()