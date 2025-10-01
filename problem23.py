

import marimo

__generated_with = "0.13.2"
app = marimo.App(width="medium")


@app.cell
def _():
    from sympy import divisors
    return (divisors,)


@app.cell
def _(divisors):
    ad = []
    for n in range(28123):
        if n < sum(divisors(n)[:-1]):
            ad.append(n)
    print(len(ad))
    return (ad,)


@app.cell
def _(ad):
    start = set(range(1,28123))
    for a in ad:
        for b in ad:
            if a+b in start:
                start.remove(a+b)
    print(len(start))
    print(sum(start))
    return


if __name__ == "__main__":
    app.run()
