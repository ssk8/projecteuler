# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "sympy==1.14.0",
# ]
# ///

import marimo

__generated_with = "0.13.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import sympy
    return (sympy,)


@app.cell
def _(sympy):
    def triangle(n):
        return sum(range(n+1))
        
    for n in range(700000):
        if len(sympy.divisors(triangle(n))) > 500:
            print(triangle(n))
            break
    return


if __name__ == "__main__":
    app.run()
