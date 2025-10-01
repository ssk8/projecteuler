

import marimo

__generated_with = "0.13.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import itertools
    return (itertools,)


@app.cell
def _():
    def p(n):
        return int(n*(3*n-1)/2)

    ps = set()

    for n in range(1, 10000):
        ps.add(p(n))
    return (ps,)


@app.cell
def _(itertools, ps):
    for j, k in itertools.combinations(ps, 2):
        if j+k in ps:
            if (j-k in ps) or (k-j in ps):
                print(j, k)
                break
    return j, k


@app.cell
def _(j, k):
    print(max(abs(j-k), k-j))
    return


if __name__ == "__main__":
    app.run()
