# T24.2 Скласти програму з графічним інтерфейсом для введення рядка та
# перевірки, чи є цей рядок паліндромом. Показати результат перевірки.

from tkinter import *


def is_palindrome(s):
    assert s
    return s == s[::-1]


def palindrome_event(s_inp):
    try:
        result = "It is a palindrome" if is_palindrome(s_inp) else "It is not a palindrome"
    except AssertionError:
        label_out.configure(text="")
    else:
        label_out.configure(text=result)


DEFAULT_FONT = ("arial", 16)

top = Tk()

frame_inputs_top = Frame(top)
frame_inputs_top.pack(fill=X, expand=YES)

frame_inputs_bottom = Frame(top)
frame_inputs_bottom.pack(fill=X, expand=YES)

frame_results = Frame(top)
frame_results.pack(fill=X, expand=YES)

Label(frame_inputs_top,
      text="Palindrome task", font=DEFAULT_FONT).pack(side=TOP)

Label(frame_inputs_bottom,
      text="Enter your string:", font=DEFAULT_FONT).pack(side=LEFT)
str_input = Entry(frame_inputs_bottom, font=DEFAULT_FONT)
str_input.pack(side=RIGHT)

Button(frame_results, text="Check", font=DEFAULT_FONT,
       command=lambda: palindrome_event(str_input.get())).pack(side=TOP)
Label(frame_results, text="Result:", font=DEFAULT_FONT).pack(side=LEFT)

label_out = Label(frame_results, text="", font=DEFAULT_FONT)
label_out.pack(side=RIGHT)

top.mainloop()
