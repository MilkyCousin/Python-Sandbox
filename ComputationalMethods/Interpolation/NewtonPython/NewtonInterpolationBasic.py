class NewtonInterpolation:
    def __init__(self, data, target):
        assert len(data) == len(target)
        self._data = data
        self._target = target
        self._l = len(self._data)

    

    def interpolate(self, x):
        ...

    def interpolate_arr(self, x):
        ...

    def get_init_points(self):
        return [self._data, self._target]

    def set_init_points(self, x, y):
        assert len(x) == len(y)
        self._data = x[:]
        self._target = y[:]