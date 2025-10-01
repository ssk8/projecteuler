import marimo

__generated_with = "0.15.5"
app = marimo.App(width="medium")


@app.cell
def _():
    from functools import cache
    return (cache,)


@app.cell
def _(cache):
    @cache
    def next_collatz(n:int) -> int:
        if n%2:
            return 3*n+1
        return n//2
    return (next_collatz,)


@app.cell
def _(next_collatz):
    def get_seq(n):
        count = 1
        while n!=1:
            count+=1
            n = next_collatz(n)
        return count

    max_count, high_start = 0, 0
    for start in range(1,1_000_000):
        if max_count  < (high:=get_seq(start)):
            max_count, high_start = high, start
    print(high_start)
    return


if __name__ == "__main__":
    app.run()
