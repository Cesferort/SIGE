# -*- coding: utf-8 -*-
class MiExcepcion (Exception):
    def __init__(self, mensaje):
        self.valor = mensaje

    def __str__(self):
        return self.valor

class Actividad10_EJ1:
    def main(self):
        try:
            user = input("Introduce usuario: ")
            password = input("Introduce contraseña: ")
            edad = int(input("Introduce edad: "))
            if edad > 100:
                raise MiExcepcion("Error: Edad complicada")
            if user == "" or password == "" or edad == "":
                raise MiExcepcion("Has introducido un valor nulo")
        except MiExcepcion as e:
            print(e)
        except:
            print("Valor no permitido")

ej1 = Actividad10_EJ1()
ej1.main()