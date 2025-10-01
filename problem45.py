

import marimo

__generated_with = "0.13.2"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    def t(n):
        return int((n*(n+1))/2)

    def p(n):
        return int((n*(3*n-1))/2)

    def h(n):
        return int(n*(2*n-1))

    ts, ps, hs = set(), set(), set()

    for n in range(2, 1000000):
        ts.add(t(n))
        ps.add(p(n))
        hs.add(h(n))
    return hs, ps, ts


@app.cell
def _(hs, ps, ts):
    print(ts&ps&hs)
    return


if __name__ == "__main__":
    app.run()
