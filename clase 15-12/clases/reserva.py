from clases.habitacion import Habitacion

class Reserva:
    def __init__(self, nombre_cliente, habitacion, num_noches):
        self.__nombre_cliente = nombre_cliente
        self.__habitacion = habitacion
        self.__num_noches = num_noches
    
    def detalles(self):
        return (f"Nombre: {self.__nombre_cliente} | "
                f"Habitacion: {self.__habitacion.get_tipo()} {self.__habitacion.get_numero()} | "
                f"Noches: {self.__num_noches} | "
                f"Precio total: {self.__habitacion.calcular_precio(self.__num_noches)}")
    