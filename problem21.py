

import marimo

__generated_with = "0.13.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import sympy
    from itertools import chain
    return chain, sympy


@app.cell
def _(sympy):
    pairs = set()
    for n in range(10000):
        pair = (n, sum(sympy.divisors(n)[:-1]))
        if len(set(pair)) == 2:
            pairs.add(pair)
    return (pairs,)


@app.cell
def _(chain, pairs):
    amicable = pairs & set(p[::-1] for p in pairs)
    sum(set(chain.from_iterable(amicable)))
    return


if __name__ == "__main__":
    app.run()
