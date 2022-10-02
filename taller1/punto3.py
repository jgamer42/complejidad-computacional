import random
def llenar_vector(tamaño_vector:int)->None:
    i = 0
    datos = []
    while i < tamaño_vector:
        datos.append(int(random.randrange(1000,9999)))
        i += 1
#Complejidad pasos O(n)
#Complejidad  memoria O(n)
# pasos 6n+2 