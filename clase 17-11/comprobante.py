from documento import Documento

class Comprobante(Documento):
    def __init__(self, id, fecha, monto):
        super().__init__(id, fecha)        
        self.__monto = monto

    @property
    def monto(self):
        return self.__monto
    
    @monto.setter
    def monto(self, monto):
        if monto <= 0:
            return "El monto debe ser mayor que 0."
        self.__monto = monto