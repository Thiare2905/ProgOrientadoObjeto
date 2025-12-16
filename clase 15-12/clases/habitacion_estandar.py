from clases.habitacion import Habitacion

class Habitacion_Estandar(Habitacion):
    # def __init__(self, numero, precio_base):
    #     super().__init__(numero, precio_base)

    # def calcular_precio(self, noches):
    #     return super().calcular_precio(noches)
    
    def get_tipo(self):
        return "Estandar"