import marimo

__generated_with = "0.16.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import numpy as np
    primes = np.genfromtxt("/home/curt/Documents/projecteuler/prime.txt", dtype=int)[1:]#78_499]
    return np, primes


@app.cell
def _(np, primes):
    n = 600_851_475_143
    #n=13195
    primes[np.where(n%primes==0)]

    return


if __name__ == "__main__":
    app.run()
