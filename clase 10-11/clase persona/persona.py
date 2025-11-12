import re

class Persona:
    def __init__(self, nombre, apellido, telefono, correo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono
        self.__correo = correo

    def get_nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"

    @property    
    def correo(self):
        return self.__correo
    
    def set_correo(self, nuevo_correo):
        valido = re.match(r'^[a-z0-9]+[. _]?[a-z0-9]+[@]\w+[.]\w+$', nuevo_correo)
        if valido:
            self.__correo = nuevo_correo
            return True
        return False
    
    def set_telefono(self, nuevo_telefono):
        valido = re.match(r'^(?:\+?56)?\s?9\s?\d{8}$', nuevo_telefono)
        if valido:
            self.__telefono = nuevo_telefono
            return True
        else:
            return False