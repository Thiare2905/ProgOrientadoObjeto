from factura import Factura

fac = Factura(101, "2025-07-09", 15000, "12.345.678-9")
print(fac.resumen_factura())

fac2 = Factura(None, None, None, "12.345.678-9")
fac2.id = 101
fac2.fecha = "2025-09-07"
fac2.monto = 150000

print(fac2.resumen_factura())
