def son_anagramas(a, b):
    a.strip()       # Quita espacios en blanco del principio y final 
    b.strip()       # Quita espacios en blanco del principio y final 
    a.lower()       # Pone todas las lteras en minuscula (normalizar)
    b.lower()       # Pone todas las lteras en minuscula (normalizar)

    aux = 0         # Auxiliar para verificar

    if len(a) == len(b):            # Si son iguales se deben comparar
        largo = len(a)              # Largo de la cadena de texto
        for i in range(len(a)):     # Recorre la cadena de texto 
            if a[i] == b[largo-1]:  # Compara el primer caracter de la primera palabra y el ultimo de segunda, y va avanzando
                largo -= 1          # Para ir retrocediento por caracter
                aux += 1            # Para después verficar
        if aux == len(a):           # Verifica que el auxiliar y el largo sean iguales
            return True             # True si son anagramas 
    else:                           # False si no lo son
        return False 

a = input("Ingrese la primera palabra: ")
b = input("Ingrese la segunda palabra: ")

if son_anagramas(a, b) == True:
    print("La palabra " + a + " y la palabra " + b + " SI son anagramas")
else:
    print("La palabra " + a + " y la palabra " + b + " NO son anagramas")

#--- Solución profesor -------------------------------------------------------------------------------------------------------------
def es_anagrama(a:str, b:str) -> bool:
    a_min = a.lower()
    b_min = b.lower()

    temp_a = []
    for ch in a_min:
        if not ch.isspace():
            temp_a.append(ch)
    a = "".join(temp_a) 
    
    temp_b = []
    for ch in b_min:
        if not ch.isspace():
            temp_b.append(ch)
    b = "".join(temp_b)         

result = es_anagrama("Amor", "Roma")