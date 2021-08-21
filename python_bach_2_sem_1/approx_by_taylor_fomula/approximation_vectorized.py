# T20.3 Виконати наближення функції f(x) на відрізку [a, b] частиною ряду Тейлора, що є
# розкладом f(x) у 0. Взяти перші n доданків для n = 1, 2, ..., m, де m – задане число.
# Побудувати графіки функції та її наближення. Зберегти відео (виконати анімацію) для
# різних значень n. Використати масиви numpy.
# Розв’язати задачу для функції f(x):
# f(x) = 1/(1+x)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def f(t):
    return 1/(1+t)


def f_taylor(t, deg=0):
    if not deg:
        return np.ones_like(t)
    else:
        # definitely could be more optimized
        powered = ((-1) * t) ** deg
        to_sum = np.vstack((powered, f_taylor(t, deg-1)))
        return np.sum(to_sum, axis=0)


c = 0
e = 0.99
x = np.linspace(c-e, c+e)

K = 50  # number of steps
T = 200  # interval between frames

fig = plt.figure()
ax = plt.axes(xlim=(c-e, c+e), ylim=(0, c+2*e))
ax.grid()
line, = ax.plot([], [])


def init_animation():
    line.set_data([], [])
    return line,


def animate(k):
    line.set_data(x, f_taylor(x, deg=k))
    line.set_label("taylor approx, k = " + str(k))
    ax.legend()
    return line,


plt.plot(x, f(x), linestyle="--", label="f(x)")

anim = animation.FuncAnimation(
    fig, animate, init_func=init_animation,
    frames=K, interval=T, blit=False
)

anim.save(filename="function_approximation.gif", writer="pillow")
