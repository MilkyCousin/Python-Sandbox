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
import matplotlib.pyplot as plt


class LagrangeInterpolationPoly:

    def __init__(self, x_net, y_net):
        assert np.all(np.diff(x_net) > 0)
        self._net = x_net
        self._target = y_net

    def basis_poly(self, x, k):
        x_k = self._net[k]
        x_net_matrix = np.repeat(np.matrix(self._net), len(x), axis=0).T
        x_net_matrix = np.delete(x_net_matrix, k, axis=0)
        denominator = 1 / (x_k - x_net_matrix)
        nominator = (x - x_net_matrix)
        return np.prod(nominator / denominator, axis=0)

    def interpolate(self, x):
        s = 0
        for k in range(len(self._net)):
            s += self.basis_poly(x, k) * self._target[k]
        return s

    def get_net(self):
        return self._net


if __name__ == "__main__":
    x_net = [1, 2, 3]
    y_net = [1, 4, 9]
    LP = LagrangeInterpolationPoly(x_net, y_net)

    X = np.linspace(0, len(x_net))
    Y = LP.interpolate(X)
    plt.hlines(0, 0, 3, linestyle='--')
    plt.plot(X,Y.T)

    for k in range(len(x_net)):
        plt.plot(X,LP.basis_poly(X, k).T)

    plt.show()
