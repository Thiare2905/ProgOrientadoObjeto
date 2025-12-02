from clases.empleado import Empleado

comision = 1.10

class Empleado_comision(Empleado):

    def calcular_pago(self):
        return super().get_salario() * comision
    