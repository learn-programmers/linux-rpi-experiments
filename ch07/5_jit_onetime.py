import numpy as np
import time
from numba import jit

# 성능 향상 전 함수
def dot_product_no_jit(a, b):
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result

# 성능 향상 후 함수
@jit(nopython=True)
def dot_product_jit(a, b):
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result

a = np.random.rand(100000)
b = np.random.rand(100000)

# 성능 향상 전 함수 실행 시간 측정
start_time = time.time()
result_no_jit = dot_product_no_jit(a, b)
elapsed_time_no_jit = time.time() - start_time
print(f"Result (no JIT): {result_no_jit:.4f}, Time: {elapsed_time_no_jit:.4f} seconds")

# 성능 향상 후 함수 실행 시간 측정
start_time = time.time()
result_jit = dot_product_jit(a, b)
elapsed_time_jit = time.time() - start_time
print(f"Result (JIT): {result_jit:.4f}, Time: {elapsed_time_jit:.4f} seconds")

