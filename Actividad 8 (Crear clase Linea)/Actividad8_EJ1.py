# -*- coding: utf-8 -*-
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return("("+ str(self.x) + ", " + str(self.y) +")")

class Linea:
    def __init__(self, x1, y1, x2, y2):
        self.puntoA = Punto(x1, y1)
        self.puntoB = Punto(x2, y2)

    def desplazaDer(self, distancia):
        self.puntoA.x += distancia
        self.puntoB.x += distancia

    def desplazaIzq(self, distancia):
        self.puntoA.x -= distancia
        self.puntoB.x -= distancia

    def desplazaArr(self, distancia):
        self.puntoA.y += distancia
        self.puntoB.y += distancia

    def desplazaAba(self, distancia):
        self.puntoA.y -= distancia
        self.puntoB.y -= distancia

    def modificar(self):
        datosValidos = False
        while datosValidos == False:
            try:
                self.puntoA.x = float(input("Introduce nuevo valor para X del Punto A: "))
                self.puntoA.y = float(input("Introduce nuevo valor para Y del Punto A: "))
                self.puntoB.x = float(input("Introduce nuevo valor para X del Punto B: "))
                self.puntoB.y = float(input("Introduce nuevo valor para Y del Punto B: "))
                datosValidos = True
            except:
                print("Valor no permitido.\nVuelve a intentarlo.")

    def __str__(self):
        resultado = ("Punto A: " + self.puntoA.__str__())
        resultado +=("\tPunto B: " + self.puntoB.__str__())
        return resultado

linea = Linea(3, 2, 4, 6)
print("Linea inicial:")
print(linea.__str__())
print()

linea.desplazaIzq(3)
print("Linea desplazada a la izquierda 3 puntos:")
print(linea.__str__())
print()

try:
    n = int(input("Introduce distancia a desplazar hacia arriba: "))
    linea.desplazaArr(n)
    print("Linea desplazada hacia arriba " + str(n) + " puntos:")
    print(linea.__str__())
except:
    print("Valor no permitido.")
print()

linea.modificar()
print("Linea modificada:")
print(linea.__str__())
print()

linea.desplazaAba(2)
print("Linea desplazada hacia abajo 2 puntos:")
print(linea.__str__())
linea.desplazaDer(4)
print("Linea desplazada a la derecha 4 puntos:")
print(linea.__str__())
print()

linea2 = linea
print("L1:")
print(linea.__str__())
print("L2:")
print(linea2.__str__())
if linea2 == linea :
    print("L1 es igual a L2? True")
else:
    print("L1 es igual a L2? False")
print()

linea3 = Linea(linea.puntoA.x, linea.puntoA.y, linea.puntoB.x, linea.puntoB.y)
print("L1:")
print(linea.__str__())
print("L3:")
print(linea3.__str__())
if linea3 == linea :
    print("L1 es igual a L3? True")
else:
    print("L1 es igual a L3? False")