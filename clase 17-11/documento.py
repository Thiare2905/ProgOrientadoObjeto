from datetime import date

class Documento:
    def __init__(self, id, fecha):
        self.__id = id
        self.__fecha = fecha

    # Valida que la fecha no esté vacía con @property y @setter
    @property
    def fecha(self):
        return self.__fecha
    
    @fecha.setter
    def fecha(self, fecha):
        if self.__fecha == '':
            raise Exception ("La fecha no puede estar vacía.")
        self.__fecha = fecha
    
    # Valida que el id sea mayor a 0 con @property y @setter
    @property
    def id(self):           # getter de id
        return self.__id
    
    @id.setter
    def id(self, id):   # setter de id
        if id < 0:
            raise Exception ("El id NO puede ser menor a 0.")
        self.__id = id