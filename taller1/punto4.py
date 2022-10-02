import random
def llenar_matriz(i:int,j:int)->None:
    datos = []
    for x in range(i):
        datos.append([])
        for y in range(j):
            datos[x].append(random.randint(1,30))

#Complejidad pasos O(n2)
#Complejidad  memoria O(n2)
# pasos (n*1)*(n*3)+1 = 3n2 + 1