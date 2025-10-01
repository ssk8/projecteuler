

import marimo

__generated_with = "0.13.2"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    all_set = set()
    for a in range(2, 5+1):
        for b in range(2,5+1):
            all_set.add(a**b)

    print(len(all_set), all_set)

    all_set = set()
    for a in range(2, 100+1):
        for b in range(2,100+1):
            all_set.add(a**b)

    print(len(all_set))
    return


if __name__ == "__main__":
    app.run()
