

import marimo

__generated_with = "0.13.2"
app = marimo.App(width="medium")


@app.cell
def _():
    dp = []
    for n in range(2,1000000):
        if sum(int(x)**5 for x in str(n)) == n:
            dp.append(n)
    print(sum(dp))
    return


if __name__ == "__main__":
    app.run()
