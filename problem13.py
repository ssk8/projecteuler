import marimo

__generated_with = "0.15.5"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    nums = []
    with open('/home/curt/Documents/projecteuler/13.txt') as file:
        lines = file.readlines()
        for line in lines:
            nums.append(int(line[:11]))
    str(sum(nums))[:10]
    return


if __name__ == "__main__":
    app.run()
