import math
import datetime
import sys

import gc

MEMO = [3, 5, 7]


def primo(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def primo_excludiding_pairs(n: int) -> bool:
    if n % 2 == 0 and n != 2:
        return False
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


def primo_sqrt(n: int) -> bool:
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def primo_with_memory(n: int) -> bool:
    global MEMO
    print(n)
    if n % 2 == 0 and n != 2:
        return False
    if n not in MEMO:
        for p in MEMO:
            print(p)
            if n % p == 0:
                return False
            if p >= int(math.sqrt(n)):
                break

    MEMO.append(n)
    return True


a = int(sys.argv[1])
# primos = []
# i = 2
# start = datetime.datetime.now()
# while len(primos) <= a:
#    if primo(i):
#        primos.append(i)
#    i += 1
# end = datetime.datetime.now()
# print(f"normal {end-start}")
# gc.collect()


# primos = []
# i = 2
# start = datetime.datetime.now()
# while len(primos) <= a:
#    if primo_excludiding_pairs(i):
#        primos.append(i)
#    i += 1
# end = datetime.datetime.now()
# print(f"pairs {end-start}")
# gc.collect()


primos = []
i = 2
start = datetime.datetime.now()
while len(primos) <= a:
    if primo_sqrt(i):
        primos.append(i)
    i += 1
end = datetime.datetime.now()
print(f"sqrt {end-start}")
print(primos)
gc.collect()


primos = []
i = 2
start = datetime.datetime.now()
while len(primos) <= a:
    if primo_with_memory(i):
        primos.append(i)
    i += 1
end = datetime.datetime.now()
print(f"memo {end-start}")
print(primos)
gc.collect()
