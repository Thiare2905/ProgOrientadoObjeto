from clases.pago import Pago

class Efectivo(Pago):
    def procesar_pago(self, monto):
        return f"Pago de {monto} procesado con efectivo."