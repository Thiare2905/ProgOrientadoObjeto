import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        result = round(math.pi * math.pow(self.radio, 2), 2)
        print ("El area es: ", result)
