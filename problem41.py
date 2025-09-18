import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    primes = []

    for n in range(9,0,-1):
        prime_file = f"/home/curt/temp_proj/primes{n}.txt"
        print(prime_file)
        with open(prime_file) as primef:
            lines = primef.readlines()
            for line in lines:
                for number in line.split():
                    primes.append(number)
    
    print(primes[:5])

    return (primes,)


@app.cell
def _(primes):
    for prime in primes:
        if set(list(prime)) == set([str(c) for c in range(1,len(prime)+1)]):
            print(prime)
    return


if __name__ == "__main__":
    app.run()
