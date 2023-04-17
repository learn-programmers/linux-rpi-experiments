import time

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

start_time = time.time()
n = 30
fib = fibonacci(n)
end_time = time.time()

print(f"Fibonacci({n}) = {fib}")
print(f"Execution time: {end_time - start_time:.4f} seconds")
