from ClaseCamas import Camas
import csv

class ManejadorCamas:
    __ListaC=[]

    def __init__(self):
        self.__ListaC=[]

    def TestListaC (self):
        archivo1=open("camas.csv")
        reader=csv.reader(archivo1,delimiter=";")
        bandera=True
        for fila in reader:
            if(bandera):
                "saltar cabecera"
                bandera=not bandera
            else:
                id = int(fila[0])
                habit= fila[1]
                est= fila[2]
                nomYapell= fila[3]
                diag= fila[4]
                fecha_i= fila[5]
                fecha_a= fila[6]
                unaCama=Camas(id,habit,est,nomYapell,diag,fecha_i,fecha_a)
                self.__ListaC.append(unaCama)


        archivo1.close()

    def __str__(self):
        s=""
        for lista in self.__ListaC:
            s+= str(lista) + "\n"
        return s

    def buscar (self, nom):
        i=0
        indice=0
        while (i<len(self.__ListaC) and (nom!= self.__ListaC[i].getNombreyApellido())):
            i+=1
            indice=i
        if i <len(self.__ListaC):
            fecha=input("Ingresar fecha de alta\n")
            self.__ListaC[indice].Agregar_alta(fecha)
            return indice
        else:
            print("Paciente incorrecto")

    def mostrarC (self, indice):
         print("Paciente:{}       Cama:{}       Habitacion:{}".format(self.__ListaC[indice].getNombreyApellido(),self.__ListaC[indice].getidCama(),self.__ListaC[indice].getHabitacion()))
         print("Diagnostico:{}              Fecha de internacion:{}".format(self.__ListaC[indice].getDiagnostico(),self.__ListaC[indice].getFecha_internacion()))
         print("Fecha de Alta:{}".format(self.__ListaC[indice].getFecha_alta()))

    def item4 (self):
        diag=input("Ingresar diagnostico")
        for  i in range (len(self.__ListaC)):
            if ((diag == self.__ListaC[i].getDiagnostico()) and (self.__ListaC[i].getEstado() == "True")):

                print("id Cama:{} - Habitacion:{} - Nombre y apellido:{} - Fecha de internacion:{}".format(self.__ListaC[i].getidCama(),self.__ListaC[i].getHabitacion(),self.__ListaC[i].getNombreyApellido(),self.__ListaC[i].getFecha_internacion()))


