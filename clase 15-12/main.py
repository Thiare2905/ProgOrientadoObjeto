from clases.reserva import Reserva
from clases.habitacion_deluxe import Habitacion_Deluxe
from clases.habitacion_estandar import Habitacion_Estandar
from clases.habitacion_suite import Habitacion_Suite

h_deluxe = Habitacion_Deluxe(11, 3500)
h_estandar = Habitacion_Estandar(30, 3500)
h_suite = Habitacion_Suite(22, 3500)

reserva1 = Reserva("Thiare Villagran", h_deluxe, 9)
reserva2 = Reserva("Alejandro Barros", h_estandar, 1)
reserva3 = Reserva("Miguel Castro", h_suite, 3)

reservas = [reserva1, reserva2, reserva3]

for r in reservas:
    print(r.detalles())






























# while True:
#     print(" - - - BIENVENIDO - - -")
#     print("1. Crear reserva.")
#     print("2. Mostrar detalles de la reserva.")
#     print("3. Salir")

#     opcion = str(input("Opción: "))

#     match opcion:
#         case "1":
#             print("Escoja habitacion...")
#             print("1. Habitacion Estandar")
#             print("2. Habitacion Suite")
#             print("3. Habitacion Deluxe")

#             match opcion:
#                 case "1":
#                     print("Agregando...")
#                 case "2":
#                     print("Agregando...")
#                 case "3":
#                     print("Agregando...")
#                 case "4":
#                     print("Saliendo...")
#                     break
#                 case _:
#                     print("Opción inválida")

#         case "2":
#             print("Eliminando...")

#         case "3":
#             print("Saliendo...")
#             break

#         case _:
#             print("Opción inválida")
