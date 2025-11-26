from .cuenta_bancaria import Cuenta_bancaria

SOBREGIRO_MAX = -500
class Cuenta_corriente(Cuenta_bancaria):
    
    def depositar(self, monto):
        return super().depositar(monto)
    
    def retirar(self, monto):
        if monto < 0:
            raise ValueError("El monto debe ser mayor a 0.")
        if monto >= super().mostrar_saldo():
            if (super().mostrar_saldo() - monto) < SOBREGIRO_MAX:
                raise ValueError("Se excede su sobregiro.")
            super().establecer_saldo(super().mostrar_saldo() - monto)
            