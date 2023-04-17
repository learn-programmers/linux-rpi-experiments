#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "6_matrix_multiply.c"

static PyObject *matrix_multiply_cpython(PyObject *self, PyObject *args) {
    Py_buffer a_buffer, b_buffer, result_buffer;
    Py_ssize_t a_rows, a_cols, b_cols;

    if (!PyArg_ParseTuple(args, "w*w*w*nnn", &a_buffer, &b_buffer, &result_buffer, &a_rows, &a_cols, &b_cols)) {
        return NULL;
    }

    matrix_multiply_c(a_buffer.buf, b_buffer.buf, result_buffer.buf, a_rows, a_cols, b_cols);

    PyBuffer_Release(&a_buffer);
    PyBuffer_Release(&b_buffer);
    PyBuffer_Release(&result_buffer);

    Py_RETURN_NONE;
}

static PyMethodDef MatrixMultiplyMethods[] = {
    {"matrix_multiply_cpython", matrix_multiply_cpython, METH_VARARGS, "Multiply two matrices"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef matrix_multiply_cpython_module = {
    PyModuleDef_HEAD_INIT,
    "matrix_multiply_cpython",
    NULL,
    -1,
    MatrixMultiplyMethods
};

PyMODINIT_FUNC PyInit_matrix_multiply_cpython(void) {
    return PyModule_Create(&matrix_multiply_cpython_module);
}
