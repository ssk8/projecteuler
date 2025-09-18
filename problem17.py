

import marimo

__generated_with = "0.13.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import num2words
    return (num2words,)


@app.cell
def _():
    len("three hundred and forty-two".translate(str.maketrans({" ":"","-":""})))
    return


@app.cell
def _(num2words):
    len(num2words.num2words(342).translate(str.maketrans({" ":"","-":""})))
    return


@app.cell
def _(num2words):
    total = 0
    for n in range(1,1001):
        total+=len(num2words.num2words(n).translate(str.maketrans({" ":"","-":""})))
    total
    return


if __name__ == "__main__":
    app.run()
