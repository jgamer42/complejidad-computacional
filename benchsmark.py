import gc
from datetime import datetime
from primos_normal import *

n_primos = 10000
primos = []
j = 2
for i in range(10):
    start_iteration = datetime.now()
    while len(primos) <= n_primos:
        start_primo = datetime.now()
        is_primo = primo(j)
        end_primo = datetime.now()
        if is_primo:
            primos.append(j)
        j += 1
        gc.collect()
    end_iteration = datetime.now()
    primos = []
    gc.collect()
    print(f"la iteracion {i} demoro {end_iteration-start_iteration} - normal")

gc.collect()
primos = []
j = 2
for i in range(10):
    start_iteration = datetime.now()
    while len(primos) <= n_primos:
        start_primo = datetime.now()
        is_primo = primo_excludiding_pairs(j)
        end_primo = datetime.now()
        if is_primo:
            primos.append(j)
        j += 1
        gc.collect()
    end_iteration = datetime.now()
    primos = []
    gc.collect()
    print(f"la iteracion {i} demoro {end_iteration-start_iteration} - pares")
gc.collect()
primos = []
j = 2
for i in range(10):
    start_iteration = datetime.now()
    while len(primos) <= n_primos:
        start_primo = datetime.now()
        is_primo = primo_sqrt(j)
        end_primo = datetime.now()
        if is_primo:
            primos.append(j)
        j += 1
        gc.collect()
    end_iteration = datetime.now()
    primos = []
    gc.collect()
    print(f"la iteracion {i} demoro {end_iteration-start_iteration} - raiz")

gc.collect()
primos = []
j = 2
for i in range(10):
    start_iteration = datetime.now()
    while len(primos) <= n_primos:
        start_primo = datetime.now()
        is_primo = primo_with_memory(j)
        end_primo = datetime.now()
        if is_primo:
            primos.append(j)
        j += 1
        gc.collect()
    end_iteration = datetime.now()
    primos = []
    gc.collect()
    print(f"la iteracion {i} demoro {end_iteration-start_iteration} - meomoria")
