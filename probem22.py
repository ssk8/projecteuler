import marimo

__generated_with = "0.15.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import polars as pl
    return (pl,)


@app.cell
def _():
    def score_name(name: str) -> int:
        return sum(map(ord, name)) - 64 * len(name)

    score_name('COLIN')
    return (score_name,)


@app.cell
def _(pl, score_name):
    names = pl.read_csv('/home/curt/Documents/projecteuler/0022_names.txt', has_header=False).transpose()
    names = names.rename({'column_0': 'name'})
    names = names.sort('name')
    names = names.with_row_index(offset=1)
    names = names.with_columns(pl.col('name').map_elements(score_name).alias('name_score'))
    names = names.with_columns((pl.col('name_score')*pl.col('index')).alias('score'))
    return (names,)


@app.cell
def _(names):
    names
    return


@app.cell
def _(names):
    print(names[937])
    return


@app.cell
def _(names, pl):
    names.select(pl.sum('score')) == 871198282
    return


if __name__ == "__main__":
    app.run()
