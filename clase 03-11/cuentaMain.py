from cuentaClase import CuentaBancaria

cuenta = CuentaBancaria(232425, "Juan Peréz", 2000)

print(cuenta.mostrarDatos())

cuenta.depositar(5000)
print(cuenta.mostrarDatos())

cuenta.retirar(30000)
print(cuenta.mostrarDatos())
