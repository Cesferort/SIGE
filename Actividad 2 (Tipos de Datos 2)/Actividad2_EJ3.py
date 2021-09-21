# -*- coding: utf-8 -*-
class Actividad2_EJ3:
    def main(self):
        print(  """
                ---------------------------------------------------
                                    TUPLAS
                ---------------------------------------------------
                """)
        print("TODAS LAS NOTAS")
        alumnado = ("Aitor", "Amaia", "Mikel", "Ainara", "Juanjo", "Asier", "Aitor")
        notasSige = (5, 3, 8, 4, 6, 2)
        notasAdat = (4, 9, 1, 7, 8, 6)

        print("TODAS LAS NOTAS")
        print(alumnado)
        output = "SIGE: "
        output += str(notasSige)
        output += " ADAT "
        output += str(notasAdat)
        print(output)

        #Notas de los primeros 3 alumnos
        print("\nNOTAS SIGE de los 3 primeros alumnos")
        print(alumnado[0:3])
        print(notasSige[0:3])

        print("\n")
        print(alumnado[notasSige.__len__() - 3:notasSige.__len__()])
        print(notasSige[notasSige.__len__() - 3:notasSige.__len__()])

ej3 = Actividad2_EJ3()
ej3.main()