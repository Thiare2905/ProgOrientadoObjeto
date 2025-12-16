from clases.habitacion import Habitacion

cargo_fijo = 200

class Habitacion_Suite(Habitacion):
    def __init__(self, numero, precio_base):
        super().__init__(numero, precio_base)

    def calcular_precio(self, noches):
        return super().calcular_precio(noches) + cargo_fijo
    
    def get_tipo(self):
        return "Suite"