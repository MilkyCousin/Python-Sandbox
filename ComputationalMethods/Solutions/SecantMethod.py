def secant_method(f, a, b, eps=10e-8):
    x0 = a
    x1 = b
    x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
    while abs(x1 - x2) >= eps:
        x1, x2 = x2, x2 - f(x2) * (x2 - x1) / (f(x2) - f(x1))
    return x2


if __name__ == "__main__":
    h = lambda t: t ** 2 - 1
    print(secant_method(h, 0.5, 1.5))

    p = lambda t: t ** 5 - 4 * t ** 3 + 3 * t ** 2 + 2 * t - 17
    print(secant_method(p, 0, 3))

    import math
    g = lambda t: math.exp(t) * math.sin(t)
    print(secant_method(g, -3.5, -2.5))