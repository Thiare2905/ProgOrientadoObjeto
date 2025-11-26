from .cuenta_bancaria import Cuenta_bancaria

FACTOR_INTERES = 1.02
class Cuenta_ahorro(Cuenta_bancaria):
    # def __init__(self, saldo):
    #     super().__init__(saldo)
    
    def consultar_saldo(self):
        return super().mostrar_saldo() * FACTOR_INTERES