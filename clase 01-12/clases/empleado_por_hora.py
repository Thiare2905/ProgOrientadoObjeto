from clases.empleado import Empleado

tarifa = 10000

class Empleado_por_hora(Empleado):
    def __init__(self, horas):
        super().__init__()
        self.__horas = horas

    def calcular_pago(self):
        return tarifa * self.__horas