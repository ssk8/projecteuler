import marimo

__generated_with = "0.16.2"
app = marimo.App(width="medium")


@app.cell
def _():
    for a in range(1, 1000):
        for b in range(1, 1000):
            for c in range(1, 1000):
                if a**2+b**2==c**2 and a+b+c==1000:
                    print(a, b, c, a*b*c)
                    break
    return


if __name__ == "__main__":
    app.run()
