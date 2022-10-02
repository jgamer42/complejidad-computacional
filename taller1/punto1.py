import math
def primo_sqrt(n:int)->bool:
    if n%2==0: #2
        return False #1
    for i in range(2,int(math.sqrt(n))+1):#3
        if n % i == 0:#2
            return False#1
    return True

#Complejidad pasos O(Raiz(N))
#Complejidad  memoria O(0
# pasos (5n + 1 + 3) = 5n+4