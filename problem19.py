import marimo

__generated_with = "0.16.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import datetime
    return (datetime,)


@app.cell
def _(datetime):
    start = datetime.date(1901, 1, 1)
    end = datetime.date(2000, 12, 31)

    days = 0
    for d in range(9999999999):
        day = start+datetime.timedelta(days=d)
        if day>end:
            break
        if day.isoweekday()==7 and day.day==1:
            days+=1
    print(days)
    return


if __name__ == "__main__":
    app.run()
