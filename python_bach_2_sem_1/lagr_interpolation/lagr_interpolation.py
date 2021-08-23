# T20.5 Нехай ми маємо послідовність точок (x0, y0), (x1, y1), …, (xn, yn).
# При цьому, x0 < x1 < … < xn. Будемо вважати, що точки yi є значеннями деякої
# функції f у точках xi. Інтерполяцією називається побудова функції f у всіх
# точках на проміжку [x0, xn].
# Одним із способів інтерполяції є застосування інтерполяційного поліному
# Лагранжа, який будується за формулою:
#                                                               x  - x_i
# P_L(x) = sum_{k=0..n}[y_k * L_k], L_k = prod_{i=0..n: i!=k}[-----------]
#                                                              x_k - x_i
# Виконати наближення інтерполяційним поліномом Лагранжа функції sin(x)
# на відрізку [0, 2π] у (n+1) точці, де n = 2k, k = 2, 3, 4, …
# (скласти функцію для обчислення PL(x))
# Використати масиви numpy. Зобразити на графіках функції sin(x) та PL(x).
# Зберегти відео (виконати анімацію) для різних значень k.

import numpy as np


class LagrangeInterpolationPoly:

    def __init__(self, x_net):
        assert np.all(np.diff(x_net) > 0)
        self._net = x_net

    def basis_poly(self, x, k):
        pass

    def interpolate(self, x, y):
        pass

    def get_net(self):
        return self._net


def L_k(x, x_net, k):
    """
    :param x: point on real line
    :param x_net: column vector of nodes
    :param k: number of component to fix
    :return: L_k(x)
    """
    X_NET = np.delete(np.matrix(np.repeat(x_net, x_net.shape[0], axis=1)).T, k, axis=1)
    X = np.matrix(np.repeat(x, x_net.shape[0], axis=1)).T
    nominator_to_multiply = (X - X_NET)
    denominator_to_multiply = 1/(x_net[k] - X_NET)
    ratio_to_multiply = nominator_to_multiply/denominator_to_multiply
    return np.prod(ratio_to_multiply, axis=1)


test_net = np.matrix(np.arange(0, 1+0.25, 0.25)).T
print(test_net)
J = L_k(1.7, test_net, 1)
print(J)
