import marimo

__generated_with = "0.15.5"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    f1, f2 = 1, 1

    for n in range(3, 5000):
        f1, f2 = f2, f1+f2
        if len(str(f2))>999:
            print(n)
            break
    
    return


if __name__ == "__main__":
    app.run()
