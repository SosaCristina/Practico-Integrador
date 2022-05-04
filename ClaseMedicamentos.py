class Medicamentos:
    __idCama2=0
    __idMedicamento= 0
    __nombre_comercial=""
    __monodroga=""
    __presentacion=""
    __cant_aplicada=0
    __precio_total=0

    def __init__(self, idC2, idM, nomC, mono, pres, cant, precio):
        self.__idCama2=idC2
        self.__idMedicamento=idM
        self.__nombre_comercial=nomC
        self.__monodroga=mono
        self.__presentacion=pres
        self.__cant_aplicada=cant
        self.__precio_total=precio



    def getidCama2 (self):
        return self.__idCama2
    def getidMedicamento (self):
        return self.__idMedicamento
    def getnom_comercial (self):
        return self.__nombre_comercial
    def getmonodroga (self):
        return self.__monodroga
    def getpresentacion(self):
        return self.__presentacion
    def getcant_aplicada(self):
        return self.__cant_aplicada
    def getprecio (self):
        return self.__precio_total

    def calculo (self):
        imp= int
        imp= int(self.__precio_total) * int(self.__cant_aplicada)
        return imp

    def __str__(self):
        return "%s %s %s %s %s %s %s" %(self.__idCama2,self.__idMedicamento,self.__nombre_comercial,self.__monodroga,self.__presentacion,self.__cant_aplicada,self.__precio_total)
