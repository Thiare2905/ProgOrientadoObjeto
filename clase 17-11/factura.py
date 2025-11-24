from comprobante import Comprobante

class Factura(Comprobante):
    def __init__(self, id, fecha, monto, rut_cliente):
        super().__init__(id, fecha, monto)
        self.__rut_cliente = rut_cliente

    # def resumen_factura(self):
    #     return f"Factura ID: {self.id} | Fecha: {self.fecha} | Monto: {self.monto} | Cliente: {self.__rut_cliente}"

    def resumen_factura(self):
        return f"Factura ID: {super().id} | Fecha: {super().fecha} | Monto: {super().monto} | Cliente: {self.__rut_cliente}"