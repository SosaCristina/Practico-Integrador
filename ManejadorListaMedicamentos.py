from ClaseMedicamentos import Medicamentos
import csv

class ManejadorMaedicamentos:
    __ListaM=[]

    def __init__(self):
        self.__ListaM=[]


    def TestListaM (self):
        archivo2=open("medicamentos.csv")
        reader=csv.reader(archivo2,delimiter=";")
        bandera=True
        for fila in reader:
            if(bandera):
                "saltar cabecera"
                bandera=not bandera
            else:
                idC2 = int(fila[0])
                idM= fila[1]
                nomC= fila[2]
                mono= fila[3]
                pres= fila[4]
                cant= fila[5]
                precio= fila[6]
                unMedicamento=Medicamentos(idC2, idM, nomC, mono, pres, cant, precio)
                self.__ListaM.append(unMedicamento)

        archivo2.close()

    def __str__(self):
        s=""
        for lista in self.__ListaM:
            s+= str(lista) + "\n"
        return s

    def mostrarM (self, indice):
        total=0
        print("Medicamento  Presentacion  Cantidad      Precio")
        for i in range (len(self.__ListaM)):
            if(self.__ListaM[i].getidCama2() == (indice+1)):
                total+=self.__ListaM[i].calculo()
                print("{}   -   {}   -   {}   -   {}   ".format(self.__ListaM[i].getnom_comercial(),self.__ListaM[i].getpresentacion(),self.__ListaM[i].getcant_aplicada(),self.__ListaM[i].getprecio()))
        print("Total Adeudado:                          ",total)


