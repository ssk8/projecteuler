import marimo

__generated_with = "0.16.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import numpy as np
    primes = np.genfromtxt("/home/curt/Documents/projecteuler/prime.txt", dtype=int)[1:78_499]
    return np, primes


@app.cell
def _(np, primes):
    fdp = primes[np.where((primes>999) & (primes<10000))]

    for prime in fdp:
        for n in range(1,10_000):
            if (prime+n in fdp) and (prime+2*n in fdp):
                if set(str(prime)) == set(str(prime+n)) == set(str(prime+2*n)):
                    print(f"{prime}{prime+n}{prime+2*n}")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
