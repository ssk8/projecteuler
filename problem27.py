

import marimo

__generated_with = "0.13.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import numpy as np
    primes = np.genfromtxt("/home/curt/Documents/projecteuler/prime.txt", dtype=int)[1:]
    return (primes,)


@app.cell
def _(primes):
    for prime in primes[:10]:
        print(prime)
    return


@app.cell
def _(primes):
    a, b = -79, 1601
    print(a*b)
    max_con = 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            this_max_con = 0
            for n in range(100):
                if n*n + a*n + b in primes:
                    this_max_con+=1
                else:
                    break
            if this_max_con>max_con:
                max_con = this_max_con
                print(max_con, a*b)

    print(max_con)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
