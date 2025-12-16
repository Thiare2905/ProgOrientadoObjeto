from clases.habitacion import Habitacion

recargo = 1.2

class Habitacion_Deluxe(Habitacion):
    def __init__(self, numero, precio_base):
        super().__init__(numero, precio_base)

    def calcular_precio(self, noches):
        return super().calcular_precio(noches) * recargo
    
    def get_tipo(self):
        return "Deluxe"