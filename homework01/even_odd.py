try:
    from numpy.random import default_rng

except:
    import numpy.random as npr
    def default_rng():
        return npr

def rand(n):
    rng = default_rng()
    return rng.choice(2*n, size=n, replace=False)

def even(a):
    e = ["even" if (a[i]%2 == 0) else "odd" for i in range(len(a)) ]
    for i in range(len(e)):
        print(a[i]," is ",e[i])

n = 10

even(rand(n))
