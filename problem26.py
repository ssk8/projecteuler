

import marimo

__generated_with = "0.13.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import decimal
    return (decimal,)


@app.cell
def _(decimal):
    decimal.getcontext().prec=3000
    max_repeat = 5

    for den in range(6,1000):
        frac_str = str(decimal.Decimal(1)/decimal.Decimal(den))[2:]
        for n in range(6,1500):
            if frac_str[:n] == frac_str[n:2*n]:
                if n>max_repeat:
                    max_repeat=n
                    print(f"denomenator = {den}, repeat seq length = {n}")
                break

    return


if __name__ == "__main__":
    app.run()
