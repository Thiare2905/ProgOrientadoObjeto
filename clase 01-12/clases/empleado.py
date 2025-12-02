class Empleado:
    def __init__(self, ):
        self.__salario = 0

    def get_salario(self):
        return self.__salario
    
    def set_salario(self, monto):
        if monto > 0:
            self.__salario = monto
            return self.__salario
        ValueError("El monto debe ser mayor a 0.")

    def calcular_pago(self):
        return self.__salario