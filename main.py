from ClaseCamas import Camas
from ClaseMedicamentos import Medicamentos
from ManejadorListaCamas import ManejadorCamas
from ManejadorListaMedicamentos import ManejadorMaedicamentos

import csv


if __name__=="__main__":

    objetoCama = ManejadorCamas()
    print("Lista de camas con sus datos")
    objetoCama.TestListaC()
    print(objetoCama)
    print("_______________________________________")
    objetoMedic = ManejadorMaedicamentos()
    print ("Lista de Medicamentos con sus datos")
    objetoMedic.TestListaM()
    print(objetoMedic)
    print("_______________________________________")

    nom=input("Ingresar nombre y apellido del paciente que se le dara el alta\n")
    indice=(objetoCama.buscar(nom))
    print("----------DATOS DE PACIENTE CON ALTA---------")
    objetoCama.mostrarC(indice)
    objetoMedic.mostrarM(indice)

    print("_______________________________________")
    print("Lista de pacientes internados con sus respectivos datos")
    objetoCama.item4()
    print("_______________________________________")






