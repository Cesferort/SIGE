#-*- coding: utf-8 -*-
'''
Created on 22/11/2015

@author: Amaia
'''
#COMENTARIOS
if __name__ == '__main__':
    print ("IMPRIMIR CONSOLA:")
    print ("_________________")
    print ("print Mensaje (entre comillas)")
    print ("Egunon Mundo")
    print ("\r\r")
    print ("NUMEROS")
    print ("_______")
    Num1=23
    Num2=13
    print ("Operaciones básicas con números. Ejemplos Num1=23 y Num2=13")
    print ("Resta de números - > Resultado:",Num1 - Num2)
    print ("Suma de números + > Resultado:",Num1+Num2)
    print ("Multiplicación de números * > Resultado:",Num1*Num2)
    print ("División de números / > Resultado:",Num1/Num2)
    print ("Módulo % > Resultado:",Num1%Num2)
    print ("Exponente ** > Resultado:",Num1**Num2)
    print ("\r")
    print ("Funciones que tiene un número. Se escribe el objeto y seguido un punto. Se despliega una lista de funciones y atributos")
    print ("Suma de números. Función __add__(valor). Ejemplo Num1.__add__(Num2) > Resultado:",Num1.__add__(Num2))
    print ("\r")
    print ("Operadores and, or y not")
    print ("True and True:", True  and True)
    print ("True and False:",True and False)
    print ("True or True:", True or True)
    print ("True or False:",  True or False)
    print ("Not True:", not True)
    print ("\r")
    print ("Operadores de comparación: ==,!=,<.<=,>,>=")
    print  ("'a'=='a'",'a'=='a')
    print ("'a'=='b'",'a'=='b')
    print ("\r")

    print ("CADENAS")
    print ("_______")
    print ("Tabulador: \\t")
    sCad1="Mi  Cadena  'ñ'\tes esta" # la  ñ aparece  bien  por la primera  línea del código  fuente que indica se utiliza unicode
    sCad2='Mi  Cadena "ñ"\tes esta'
    sCad3=r"Mi Cadena \t'ñ'es  esta" # raw
    sCad4=u"Mi cadena 'ñ'\tes esta" # unicode
    sCad5=""" Mi cadena \t'ñ'es esta"""
    sCad6="Valor:"
    sCad7="esta frase es de pruebas"
    sCad8="-";
    sCad9=("a","b","c");   # Arrays  de cadenas, ver tuplas mas adelante
    sCad10="El valor de {}+{} es {}"  # Las llaves denotan  posición de los parámetros a sustituir  0, 1,2
    # Las llaves  se escapan  duplicándolas ver http://docs.python.org/2/library/string.html#formatstrings
    print ("Entre  comillas  dobles:",sCad1)
    print ("Entre  comillas  simples:",sCad2)
    print ("Cadena raw",sCad3)
    print ("Cadena unicode",sCad4)

    # Funciones   básicas:
    print("--------------Funciones básicas----------------")
    print("capitalize:", sCad7.capitalize())
    print("center:", sCad7.center(50))
    print("ljust:", sCad7.ljust(50))
    print("rjust:", sCad7.rjust(50))
    print("count(es):", sCad7.count("es"))
    print("find(se):", sCad7.find("se"))
    print("upper:", sCad7.upper())
    print("split espacios:", sCad7.split(" "))
    print("len(cadena):", len(sCad7))
    print("cadena1.join(cadena2):", sCad8.join(sCad9))
    print("format:", sCad10.format(1, 2, 1 + 2))