import marimo

__generated_with = "0.15.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import polars as pl
    return (pl,)


@app.cell
def _():
    #ori_file = '/home/curt/Documents/projecteuler/primes1.txt'
    #mod_file = '/home/curt/Documents/projecteuler/prime.csv'
    #prime = []
    #with open(ori_file) as file:
    #    for line in file.readlines():
    #        for number in line.split():
    #            prime.append(int(number))
    return


@app.cell
def _():
    #df = pl.DataFrame({'primes': prime})
    return


@app.cell
def _(pl):
    primes = pl.read_csv('/home/curt/Documents/projecteuler/prime.csv')
    return (primes,)


@app.cell
def _(pl, primes):
    #primes.filter(pl.col('primes')<10).sum()
    primes.filter(pl.col('primes')<2_000_000).sum()
    return


if __name__ == "__main__":
    app.run()
