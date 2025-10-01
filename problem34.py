import marimo

__generated_with = "0.16.2"
app = marimo.App(width="medium")


@app.cell
def _():
    from math import factorial
    return (factorial,)


@app.cell
def _(factorial):
    def is_it(n: int) -> bool:
        return sum([factorial(int(x)) for x in str(n)]) == n
    return (is_it,)


@app.cell
def _(is_it):
    total =0
    for n in range(3, 1000000):
        if is_it(n):
            total+=n
            print(n)
    print(f"{total=}")
    return


if __name__ == "__main__":
    app.run()
