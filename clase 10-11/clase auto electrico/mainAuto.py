from auto_electrico import Auto_electrico

auto = Auto_electrico(30)

print(auto.recargar(70))
print(auto.conducir2(25))
# conducir = auto.conducir(30)
# if conducir:
#     print(f"Nivel de bateria: {auto.get_bateria()}.")

# carga = auto.cargar(50)
# if carga:
#     print(f"Nivel de bateria: {auto.get_bateria()}.")
# else:
#     print("No se pudo realizar la carga.")