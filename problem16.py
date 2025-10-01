import marimo

__generated_with = "0.16.2"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    sum(int(c) for c in str(2**1000))
    return


if __name__ == "__main__":
    app.run()
