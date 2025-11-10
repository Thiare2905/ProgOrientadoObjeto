from mascota import Mascota

class Veterianaria():
    def __init__(self, nombre_veterinaria):
        self.nombre_veterinaria = nombre_veterinaria
        self.mascotas = []

    def registrar(self, mascota:Mascota):
        self.mascotas.append(mascota)

     