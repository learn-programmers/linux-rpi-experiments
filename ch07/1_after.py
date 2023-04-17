import time

def fibonacci(n):
    fib_values = [0, 1]
    
    for i in range(2, n+1):
        fib_values.append(fib_values[i-1] + fib_values[i-2])
    
    return fib_values[n]

start_time = time.time()
n = 30
fib = fibonacci(n)
end_time = time.time()

print(f"Fibonacci({n}) = {fib}")
print(f"Execution time: {end_time - start_time:.4f} seconds")




