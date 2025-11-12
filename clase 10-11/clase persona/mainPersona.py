from persona import Persona

persona = Persona("Thiare", "Villagran", "+56912345678", "correo@gmail.cl")

print(persona.get_nombre_completo())
print(persona.correo)

correo_valido = persona.set_correo("correoelec@aa.com")
if correo_valido:
    print("Correo insertado con exito.")
else:
    print("Correo invalido, revise e intente nuevamente.")

telefono_valido = persona.set_telefono("+56972783456")
if telefono_valido:
    print("Telefono insertado con exito.")
else: 
    print("Telefono invalido.")