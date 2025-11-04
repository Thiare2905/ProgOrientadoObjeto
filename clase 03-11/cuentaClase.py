class CuentaBancaria:
    def __init__(self, numeroCuenta, titular, saldo):
        self.numeroCuenta = numeroCuenta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo = self.saldo + monto

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo = self.saldo - monto
        else:
            print("No puede retirar porque excede su saldo.")

        # Otra forma de hacerlo
        # if self.saldo < monto:
        #     raise Exception("Saldo insuficiente")
        # self.saldo -= monto

    def mostrarDatos(self):
        return f"Cuenta: {self.numeroCuenta}\nTitular: {self.titular}\nSaldo: {self.saldo}\n"