import sys
sys.setrecursionlimit(1000000)

import time
from typing import final

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

def factoria_n(n):
    if n == 1:
        return 1

    return n * factoria_n(n -1)

if __name__ == '__main__':
    n = 10000

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factoria_n(n)
    final = time.time()
    print(final - comienzo)