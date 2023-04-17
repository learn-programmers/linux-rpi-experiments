import multiprocessing

def square(x):
    return x * x

if __name__ == "__main__":
    pool = multiprocessing.Pool()
    results = pool.map(square, [1, 2, 3, 4, 5])
    print(results)
