from clases.pago import Pago

class Tarjeta(Pago):
    def procesar_pago(self, monto):
        return f"Pago de {monto} procesado con tarjeta."