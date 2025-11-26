from clases.cuenta_ahorro import Cuenta_ahorro
from clases.cuenta_corriente import Cuenta_corriente

cuenta = Cuenta_ahorro(5000)
cuentaC = Cuenta_corriente(5000)

cuentaC.retirar(5000)
print(cuentaC.mostrar_saldo())
