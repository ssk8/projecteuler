import marimo

__generated_with = "0.15.5"
app = marimo.App(width="medium")


@app.cell
def _():
    from itertools import permutations, islice
    return islice, permutations


@app.cell
def _(islice, permutations):
    print(''.join(list(islice(permutations("0123456789"), 999_999, 1_000_000))[0]))
    return


if __name__ == "__main__":
    app.run()
