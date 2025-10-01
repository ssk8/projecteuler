import marimo

__generated_with = "0.16.2"
app = marimo.App(width="medium")


@app.cell
def _():
    from math import factorial
    return (factorial,)


@app.cell
def _(factorial):
    sum(int(c) for c in str(factorial(100)))
    return


if __name__ == "__main__":
    app.run()
