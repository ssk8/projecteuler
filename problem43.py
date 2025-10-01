

import marimo

__generated_with = "0.13.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import itertools
    return (itertools,)


@app.cell
def _(itertools):
    def ssd(n: list[str])->bool:
        for i, d in enumerate((2, 3, 5, 7, 11, 13, 17), 1):
            if int("".join(n[i:i+3]))%d: return False
        return True

    n = [c for c in "1406357289"]
    print(ssd(n))

    all_ssd = []
    for n in itertools.permutations("0123456789"):
        if ssd(n):
            all_ssd.append(int("".join(n)))
        
    print(sum(all_ssd))
    return


if __name__ == "__main__":
    app.run()
