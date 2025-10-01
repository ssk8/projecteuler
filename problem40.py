

import marimo

__generated_with = "0.13.2"
app = marimo.App(width="medium")


@app.cell
def _():
    from functools import reduce
    from operator import mul
    return mul, reduce


@app.cell
def _():
    cc = [0]
    with open('/home/curt/Documents/projecteuler/b033307.txt') as file:
        for l in file.readlines():
            try:
                cc.append(int(l[-2]))
            except Exception as e:
                print(e)
    for m in range(5):
        print(cc[10**m])
    return


@app.cell
def _(mul, reduce):
    def get_pos(n):
        digit_length, count, start = 1, 9 ,1

        while n > digit_length * count:
            n -= digit_length * count
            digit_length += 1
            count *= 10
            start *= 10

        number = start + (n - 1) // digit_length
        digit_index = (n - 1) % digit_length

        return int(str(number)[digit_index])


    for n in range(5):
        print(get_pos(10**n))

    print(reduce(mul, [get_pos(10**n) for n in range(7)]))

    return


if __name__ == "__main__":
    app.run()
