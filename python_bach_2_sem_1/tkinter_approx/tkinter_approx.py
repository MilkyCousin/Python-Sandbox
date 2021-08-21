# Скласти програму з графічним інтерфейсом для введення x, ε та
# обчислення суми усіх доданків, які за абсолютною величиною не менші ε:
#         1
# y = --------- = 1 - 2 * x + 3 * x^2 - ... (|x| < 1)
#     (1 + x)^2
# Проконтролювати виконання умови |x| < 1. Показати результат обчислень.

from tkinter import *


def f(x):
    return 1/(1 + x) ** 2


def approx(x, eps):
    assert abs(x) < 1 and eps > 0
    s0 = 1
    s1 = s0 - 2*x
    j = 2
    while abs(s1 - s0) > eps:
        s0, s1 = s1, s1 + (-1) ** j * (j + 1) * x ** j
        j += 1
    return s1


def approx_event(x_inp, eps_inp):
    try:
        x_num = float(x_inp)
        eps_num = float(eps_inp)
        approx_val = approx(x_num, eps_num)
    except ValueError:
        label_out.configure(text="Invalid values occurred")
    except AssertionError:
        label_out.configure(text="|x| >= 1 or eps <= 0")
    else:
        label_out.configure(text="%g" % approx_val)


DEFAULT_FONT = ("arial", 16)

top = Tk()

frame_inputs_top = Frame(top)
frame_inputs_top.pack(fill=X, expand=YES)

frame_inputs_bottom = Frame(top)
frame_inputs_bottom.pack(fill=X, expand=YES)

frame_results = Frame(top)
frame_results.pack(fill=X, expand=YES)

Label(frame_inputs_top, text="Approximation task",
      font=DEFAULT_FONT).pack(side=TOP)

Label(frame_inputs_top, text="Enter the value for x:",
      font=DEFAULT_FONT).pack(side=LEFT)

input_x = Entry(frame_inputs_top, font=DEFAULT_FONT)
input_x.pack(side=RIGHT)

Label(frame_inputs_bottom, text="Enter the value for eps:",
      font=DEFAULT_FONT).pack(side=LEFT)

input_eps = Entry(frame_inputs_bottom, font=DEFAULT_FONT)
input_eps.pack(side=RIGHT)

Button(frame_results, text="Calculate", font=DEFAULT_FONT,
       command=lambda: approx_event(input_x.get(), input_eps.get())).pack(side=TOP)
Label(frame_results, text="Result:", font=DEFAULT_FONT).pack(side=LEFT)

label_out = Label(frame_results, text="", font=DEFAULT_FONT)
label_out.pack(side=RIGHT)

top.mainloop()
