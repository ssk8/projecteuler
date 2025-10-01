

import marimo

__generated_with = "0.13.2"
app = marimo.App(width="medium")


@app.cell
def _():
    from itertools import permutations
    return (permutations,)


@app.cell
def _():
    def mmp(ns: str)->list[int]:
        for m1l in range(1,10):
            for m2l in range(1,10):
                if m1l+m2l<8:
                    if int(ns[:m1l])*int(ns[m1l:m1l+m2l])==int(ns[m1l+m2l:]):
                        return int(ns[m1l+m2l:])

    test = "391867254"  
    mmp(test)
    return (mmp,)


@app.cell
def _(mmp, permutations):
    pd = set()
    for ns in permutations("123456789",9):
        if p:=mmp("".join(ns)):
            pd.add(p)
    sum(pd)
    return


if __name__ == "__main__":
    app.run()
