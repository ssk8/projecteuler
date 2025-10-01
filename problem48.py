import marimo

__generated_with = "0.16.2"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    total = 0
    for n in range(1,1001):
        total+=n**n
    print("fin=", str(total)[-10:])
    return


if __name__ == "__main__":
    app.run()
