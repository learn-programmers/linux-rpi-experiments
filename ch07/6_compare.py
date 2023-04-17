import numpy as np
import time
import matrix_multiply_cpython
import ctypes

# 순수한 Python 코드로 작성한 행렬 곱셈 함수
def matrix_multiply_python(a, b):
    a_rows, a_cols = a.shape
    b_rows, b_cols = b.shape
    result = np.zeros((a_rows, b_cols))

    for i in range(a_rows):
        for j in range(b_cols):
            for k in range(a_cols):
                result[i, j] += a[i, k] * b[k, j]
    return result

# CPython 확장을 사용한 함수 호출
def matrix_multiply_cpython_wrapper(a, b):
    result = np.zeros((a.shape[0], b.shape[1]), dtype=a.dtype)
    matrix_multiply_cpython.matrix_multiply_cpython(a, b, result, a.shape[0], a.shape[1], b.shape[1])
    return result

# ctypes를 사용한 함수 호출
_multiply = ctypes.CDLL('./matrix_multiply.so')
_multiply.matrix_multiply_c.argtypes = (ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
                                         ctypes.POINTER(ctypes.c_double), ctypes.c_size_t, ctypes.c_size_t,
                                         ctypes.c_size_t)

def matrix_multiply_ctypes(a, b):
    a_rows, a_cols = a.shape
    b_rows, b_cols = b.shape
    result = np.zeros((a_rows, b_cols))

    _multiply.matrix_multiply_c(
        a.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        b.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        result.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        a_rows, a_cols, b_cols
    )
    return result

# 외부 라이브러리인 NumPy를 사용한 행렬 곱셈 함수
def matrix_multiply_numpy(a, b):
    return np.dot(a, b)

# 성능 테스트
def test_performance(matrix_multiply_func, a, b, num_iterations=10):
    start_time = time.time()

    for _ in range(num_iterations):
        matrix_multiply_func(a, b)

    end_time = time.time()
    return (end_time - start_time) / num_iterations

if __name__ == "__main__":
    a = np.random.rand(100, 200)
    b = np.random.rand(200, 150)

    num_iterations = 10

    python_duration = test_performance(matrix_multiply_python, a, b, num_iterations)
    cpython_duration = test_performance(matrix_multiply_cpython_wrapper, a, b, num_iterations)
    ctypes_duration = test_performance(matrix_multiply_ctypes, a, b, num_iterations)
    numpy_duration = test_performance(matrix_multiply_numpy, a, b, num_iterations)

    print("Python average duration: {:.6f}s".format(python_duration))
    print("CPython average duration: {:.6f}s".format(cpython_duration))
    print("ctypes average duration: {:.6f}s".format(ctypes_duration))
    print("NumPy average duration: {:.6f}s".format(numpy_duration))
