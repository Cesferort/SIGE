# -*- coding: utf-8 -*-
class Extra_Ficheros:
    def main(self):
        # 1- Abrir el fichero y asignar a una variable
        try:
            fich = open("prueba.txt","a")
        except:
            print("No se ha podido abrir el archivo")
            exit

        # 2-Tratamiento información
        print("\r\r\rSITUACiÓN ACTUAL del puntero- AL ABRIR:", fich.tell())
        fich.write("\r\r\r_____________________________________\r\r\r")
        fich.write("HOLA, Es una prueba de añadir\r")
        print("SITUACIÓN ACTUAL del puntero- TRAS ESCRIBIR:", fich.tell())

        listapalabras = ["Una ", "Dos separadas ", "tres separadas y con salto\r","\n","Quinta"]
        fich.writelines(listapalabras)

        fich.seek(0, 0)  # Posición absoluta desde el principio
        print(" SITUACIÓN ACTUAL del puntero- TRAS Mover al principio: ",fich.tell())
        print(fich.readline())  # Lee desde la posición actual lo que queda de línea.
        fich.seek(225, 0)  # Posición absoluta. Se mueve 25 bytes desde el principio
        print(" SITUACIÓN ACTUAL del puntero tras mover 25 Bytes: ",fich.tell())
        print(fich.readline())
        fich.seek(79, 1)  # Posición relativa. Se mueve 79 bytes desde la posición actual
        print(" SITUACIÓN ACTUAL del puntero tras mover 79Bytes desde la posicion anterior: ",fich.tell())
        print(fich.readline())
        fich.seek(-125, 2)  # Posición absoluta. Se mueve 125 bytes desde el final haciael principio
        print(fich.readline())

        fich.seek(0)
        print("Lee los 225 primeros bytes")
        print(fich.read(230))

        fich.seek(85, 0)
        # Readlines--> Devuelve una lista con las líneas
        print("Resultado Readlines()")
        print(fich.readlines(), "\r\r")

        fich.seek(85, 0)
        resto = fich.readlines()
        # Como es una lista, puedo leerla con un for
        print("Resultado Readlines() recorrido con for")
        for linea in resto:
            print(linea)
        print("\r\r")
        fich.seek(85, 0)
        fichero = fich.read()  # Lee todo el fichero
        print("Resultado read()\r\r", fichero)

        # Después de manipular, cerrar el fichero
        fich.close()
ej1 = Extra_Ficheros()
ej1.main()