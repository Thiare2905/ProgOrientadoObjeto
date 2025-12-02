from clases.empleado_comision import Empleado_comision
from clases.empleado_por_hora import Empleado_por_hora
from clases.empleado import Empleado

comision = Empleado_comision()
comision.set_salario(20000)
print("Su pago total es:")
print(comision.calcular_pago())

por_hora = Empleado_por_hora(2000)
print("Su pago total es:")
print(por_hora.calcular_pago())

