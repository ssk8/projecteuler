

import marimo

__generated_with = "0.13.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import sympy
    return (sympy,)


@app.cell
def _(sympy):
    cons = 4
    for start in range(100, 200_000):
        l = []
        for n in range(start, start+cons):
            l+=sympy.factorint(n).items()
        if len(set(l))==cons**2:
            print(start)
            break
    return


if __name__ == "__main__":
    app.run()
