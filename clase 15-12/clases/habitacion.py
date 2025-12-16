from abc import ABC, abstractmethod

class Habitacion(ABC):
    def __init__(self, numero, precio_base):
        self.__numero = numero
        self.__precio_base = precio_base

    def get_numero(self):
        return self.__numero
    
    def get_precio(self):
        return self.__precio_base
    
    def calcular_precio(self, noches):
        return self.__precio_base * noches
    
    def get_tipo(self):
        return ""
