class Camas:
    __idCama=0
    __habitacion= 0
    __estado = bool
    __nombreapellido= ""
    __diagnostico=""
    __fecha_internacion=""
    __fecha_alta=""

    def __init__(self, id, habit, est, nomYapell, diag, fecha_i, fecha_a):
        self.__idCama=id
        self.__habitacion=habit
        self.__estado=est
        self.__nombreapellido=nomYapell
        self.__diagnostico=diag
        self.__fecha_internacion=fecha_i
        self.__fecha_alta=fecha_a

    def getidCama (self):
         return self.__idCama
    def getHabitacion(self):
         return self.__habitacion
    def getEstado(self):
         return self.__estado
    def getNombreyApellido(self):
         return self.__nombreapellido
    def getDiagnostico(self):
         return self.__diagnostico
    def getFecha_internacion(self):
         return self.__fecha_internacion
    def getFecha_alta(self):
         return self.__fecha_alta

    def __str__(self):
        return "%s %s %s %s %s %s %s" %(self.__idCama,self.__habitacion,self.__estado,self.__nombreapellido,self.__diagnostico,self.__fecha_internacion,self.__fecha_alta)

    def Agregar_alta(self, fecha):
        self.__fecha_alta=fecha

