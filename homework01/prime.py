import numpy as np
mx = 100

ns = np.array(range(3,mx+1))
# isprime function
def isprime(e):
    return all(e%j != 0 for j in range(2, int(e/2)+1))
# list comprehension
[print(i) if isprime(i) else "" for i in ns]
