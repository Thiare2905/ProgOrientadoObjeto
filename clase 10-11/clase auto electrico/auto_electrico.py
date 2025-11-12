class Auto_electrico:
    def __init__(self, bateria):
        self.__bateria = bateria

    def get_bateria(self):
        return self.__bateria

    def cargar(self, energia):
        if energia > 0:
            aux = self.__bateria
            aux = aux + energia
            if aux <= 100:
                self.__bateria += energia
                return True
            else:
                return False
            
    def conducir(self, km):
        if km > 0 and km <= 100:
            self.__bateria -= km
            return True
        else:
            return False
# -----------------------------------------------        
    def recargar(self, recarga):
        if recarga <= 0:
            return "El valor a cargar debe ser mayor a 0"
        elif recarga + self.__bateria > 100:
            self.__bateria = 100
            return f"El valor excede su capacidad, se recargaron {100 - self.__bateria}%, se le devolvera {(self.__bateria + recarga) - 100}% en dinero."
        else:
            self.__bateria += recarga
            return f"Se recargó con exito, ahora tiene un {self.__bateria}%"
        
    def conducir2(self, km):
        if km <= 0:
            return "El valor a cargar debe ser mayor a 0"
        elif km > self.__bateria:
            return f"Usted no puede conducir {km} kilometros, su porcentaje de bateria es insuficiente."
        else: 
            self.__bateria -= km
            return f"Condujiste {km} kilometros. Te queda un {self.__bateria}% de bateria."
