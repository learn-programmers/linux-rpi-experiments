import time
import tracemalloc

# 최적화하지 않은 버전
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# 최적화한 버전
def fibonacci_optimized(n):
    if n <= 1:
        return n
    prev1 = 0
    prev2 = 1
    for i in range(2, n+1):
        current = prev1 + prev2
        prev1 = prev2
        prev2 = current
    return current

# 성능 측정 함수
def measure_performance(func, arg):
    start_time = time.time()
    result = func(arg)
    end_time = time.time()
    return result, end_time - start_time

# 메모리 사용량 측정 함수
def measure_memory_usage(func, arg):
    tracemalloc.start()
    func(arg)
    peak_memory = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    return peak_memory

if __name__ == "__main__":
    n = 35

    # 최적화하지 않은 버전
    mem_usage = measure_memory_usage(fibonacci, n)
    fib, time_elapsed = measure_performance(fibonacci, n)
    print(f"Non-optimized: Time elapsed={time_elapsed:.6f} seconds, Peak memory usage={mem_usage/1024/1024:.6f} MB")

    # 최적화한 버전
    mem_usage = measure_memory_usage(fibonacci_optimized, n)
    fib, time_elapsed = measure_performance(fibonacci_optimized, n)
    print(f"Optimized: Time elapsed={time_elapsed:.6f} seconds, Peak memory usage={mem_usage/1024/1024:.6f} MB")

