

import marimo

__generated_with = "0.13.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import numpy as np
    import sympy


    primes = np.genfromtxt("/home/curt/Documents/projecteuler/prime.txt", dtype=int)[1:78_499]

    return primes, sympy


@app.cell
def _(primes, sympy):
    def ocng():
        n = 0
        while 1:
            n+=1
            if n%2 and sympy.divisor_count(n)>2:
                yield n

    ocn = ocng()

    for _ in range(9999):
        o = next(ocn)
        for x in range(1,int(o**(1/2)+1)):
            if o - 2*x*x in primes:
                break
        else:
            print(o, x)
        
    return


if __name__ == "__main__":
    app.run()
