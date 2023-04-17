#include <stddef.h>

void matrix_multiply_c(double *a, double *b, double *result, size_t a_rows, size_t a_cols, size_t b_cols) {
    size_t i, j, k;
    for (i = 0; i < a_rows; ++i) {
        for (j = 0; j < b_cols; ++j) {
            double sum = 0;
            for (k = 0; k < a_cols; ++k) {
                sum += a[i * a_cols + k] * b[k * b_cols + j];
            }
            result[i * b_cols + j] = sum;
        }
    }
}
