from clases.tarjeta import Tarjeta
from clases.paypal import Paypal
from clases.efectivo import Efectivo

pagos = [Tarjeta(), Paypal(), Efectivo()]

for p in pagos:
    print(p.procesar_pago(100))