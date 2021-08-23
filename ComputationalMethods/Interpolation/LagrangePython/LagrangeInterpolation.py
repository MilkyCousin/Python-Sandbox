class LagrangeInterpolation:
    def __init__(self, data, target):
        assert len(data) == len(target)
        self._data = data
        self._target = target
        self._l = len(self._data)

    def basis_polynomial(self, x, k):
        assert 0 <= k < self._l
        value = 1
        for i in range(self._l):
            if i != k:
                value *= (x - self._data[i]) / (self._data[k] - self._data[i])
        return value

    def basis_polynomial_arr(self, x, k):
        return [self.basis_polynomial(x[i], k) for i in range(len(x))]

    def interpolate(self, x):
        return sum([self._target[k] * self.basis_polynomial(x, k) for k in range(self._l)])

    def interpolate_arr(self, x):
        return [self.interpolate(x[i]) for i in range(len(x))]

    def get_init_points(self):
        return [self._data, self._target]

    def set_init_points(self, x, y):
        assert len(x) == len(y)
        self._data = x[:]
        self._target = y[:]


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    x_net = [1, 2, 3]
    y_net = [1, 4, 9]
    M = 100
    K = 4
    t = list(K*i/M for i in range(-M, M+1))
    LP = LagrangeInterpolation(x_net, y_net)

    for k in range(len(x_net)):
        plt.plot(t, LP.basis_polynomial_arr(t, k), linestyle="--")

    plt.plot(t, LP.interpolate_arr(t))
    plt.show()
