import numpy as np
cimport numpy as np

ctypedef np.float64_t DTYPE_t

cpdef np.ndarray[np.float64_t, ndim=2] matrix_multiply_cython(np.ndarray[np.float64_t, ndim=2] a, np.ndarray[np.float64_t, ndim=2] b):
    cdef int i, j, k
    cdef np.ndarray[np.float64_t, ndim=2] result = np.zeros((a.shape[0], b.shape[1]))

    for i in range(a.shape[0]):
        for j in range(b.shape[1]):
            for k in range(a.shape[1]):
                result[i, j] += a[i, k] * b[k, j]
    return result
