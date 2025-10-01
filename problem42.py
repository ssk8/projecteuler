

import marimo

__generated_with = "0.13.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import json
    with open("/home/curt/Documents/projecteuler/0042_words.txt") as file:
        line = file.readline()
        words = json.loads("["+line+"]")
        for w in words:
            print(w)
    return (words,)


@app.cell
def _(words):
    def t(n: int) ->int:
        return int(n*(n+1)/2)

    ts = set()
    for n in range(1,10000):
        ts.add(t(n))

    def convert(word: str)->int:
        return sum(ord(c)-64 for c in word)

    print(convert("SKY") in ts)

    total_twords = 0
    for word in words:
        if convert(word) in ts:
            total_twords+=1

    print(total_twords)
    return


if __name__ == "__main__":
    app.run()
