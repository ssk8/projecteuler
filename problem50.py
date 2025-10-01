import marimo

__generated_with = "0.16.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import numpy as np
    return (np,)


@app.cell
def _(np):
    primes = np.genfromtxt("/home/curt/Documents/projecteuler/prime.txt", dtype=int)[1:78_499]
    primes
    return (primes,)


@app.cell
def _(primes):
    longest = 0
    for n in range(1000):
        for m in range(1000):
            if (h:=primes[n:n+m].sum())<1_000_000 and h in primes and m>longest:
                longest=m
                print(h)
    return


if __name__ == "__main__":
    app.run()
