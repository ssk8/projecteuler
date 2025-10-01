

import marimo

__generated_with = "0.13.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import itertools
    return


@app.cell
def _():
    coins = [1, 2, 5, 10, 20, 50, 100, 200][::-1]
    total = 0
    def possible(n):
        return range(0, 200+1, coins[n])

    for c0 in possible(0):
        if c0>200: break
        for c1 in possible(1):
            if sum((c0, c1))>200: break
            for c2 in possible(2):
                if sum((c0, c1, c2))>200: break
                for c3 in possible(3):
                        if sum((c0, c1, c2, c3))>200: break
                        for c4 in possible(4):
                            if sum((c0, c1, c2, c3, c4))>200: break
                            for c5 in possible(5):
                                if sum((c0, c1, c2, c3, c4, c5))>200: break
                                for c6 in possible(6):
                                    if sum((c0, c1, c2, c3, c4, c5, c6))>200: break
                                    for c7 in possible(7):
                                        if sum((c0, c1, c2, c3, c4, c5, c6, c7))==200:
                                            total+=1
                                            break
                                        elif sum((c0, c1, c2, c3, c4, c5, c6, c7))>200:
                                            break
    print(total)
    return


if __name__ == "__main__":
    app.run()
