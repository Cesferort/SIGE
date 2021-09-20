# -*- coding: utf-8 -*-
class Actividad2_EJ2:
    def main(self):
        alumnado = ["Aitor", "Amaia", "Mikel"]
        notasSige = [5, 3, 8]
        notasAdat = [4, 9, 1]

        #2.1
        i = 0
        while i < alumnado.__len__():
            print(alumnado[i])
            print("- SIGE: ", notasSige[i])
            print("- ADAT: ", notasAdat[i])
            i += 1

        #2.2
        alumnado.append("Ainara")
        notasSige.append(4)
        notasAdat.append(7)

        alumnado.append("Juanjo")
        notasSige.append(6)
        notasAdat.append(8)

        alumnado.append("Asier")
        notasSige.append(2)
        notasAdat.append(4)

        print("\nINCLUIDOS NUEVOS ALUMNOS")
        output = ""
        output += "- Alumnado actual "
        output += str(alumnado)
        print(output)

        output = ""
        output += "- SIGE: "
        output += str(notasSige)
        print(output)

        output = ""
        output += "- ADAT: "
        output += str(notasAdat)
        print(output)

        #2.3
        print("\nCALCULAR suma de 0,5 de Actitud en SIGE si la nota actual es >5")
        output = "Notas SIGE: "
        output += str(notasSige)
        print(output)

        i = 0
        while i < notasSige.__len__():
            if notasSige[i] >= 5:
                notasSige[i] = notasSige[i] + 0.5
            i += 1
        output = "+0.5 en aprobados: "
        output += str(notasSige)
        print(output)

        #2.4
        i = 0
        asierEncontrado = False
        while i < alumnado.__len__() and asierEncontrado == False:
            if alumnado[i].upper() == "ASIER":
                print("- Nota actual ", notasAdat[i])
                notasAdat[i] = 6
                print("\t- Asignación nueva ", notasAdat[i])
                asierEncontrado = True
            i += 1
        if asierEncontrado == False:
            print("No se ha podido encontrado a Asier")

ej2 = Actividad2_EJ2()
ej2.main()