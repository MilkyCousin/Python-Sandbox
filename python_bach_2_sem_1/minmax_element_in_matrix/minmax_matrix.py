# Скласти програму пошуку найменшого серед найбільших елементів
# рядків квадратної дійсної матриці порядку n, тобто
# min_{1 <= i <= n}[max_{1 <= j <= n}[a_ij]]
# Використати масиви numpy та векторизувати програмний код.

import numpy as np


def max_min(A):
    assert not np.diff(A.shape)
    return np.min(np.max(A, axis=1))


A = np.array([[1, 2, 5],
              [3, 6, -5],
              [3, -9, -2]])

print(max_min(A))
