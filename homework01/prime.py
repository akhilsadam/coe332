import numpy as np
from sympy import false, true
mx = 100

ns = np.array(range(3,mx+1))

def isprime(e):
    for j in range(2, int(e/2)+1):
        if e%j == 0:
            return false
    return true

[print(i) if isprime(i) else "" for i in ns]