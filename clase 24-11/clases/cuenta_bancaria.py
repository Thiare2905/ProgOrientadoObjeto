class Cuenta_bancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            return f"Se depositó un monto de {monto}"
        else:
            return "El monto debe ser superior a 0."
    
    def retirar(self, monto):
        if monto < 0:
            return "El monto debe ser mayor a 0."
        if self.__saldo < monto:
            return "Usted no tiene saldo sufientente."
        self.__saldo -= monto
        return f"Se retiró un monto de {monto}"

    def mostrar_saldo(self):
        return self.__saldo
        
    def establecer_saldo(self, saldo):
        self.__saldo = saldo