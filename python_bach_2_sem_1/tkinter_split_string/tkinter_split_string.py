# T24.3 Скласти програму з графічним інтерфейсом для введення рядка та
# виведення всіх різних слів цього рядка. Слова виводити у віджет список.
from string import punctuation
from tkinter import *


def split_event():
    s_inp = str_input.get()
    str_input.delete(0, END)
    list_out.delete(0, END)
    for s in set(s_inp.split()):
        if s not in punctuation:
            list_out.insert(END, s)


DEFAULT_FONT = ("arial", 16)

top = Tk()

frame_inputs_top = Frame(top)
frame_inputs_top.pack(fill=X, expand=YES)

frame_inputs_bottom = Frame(top)
frame_inputs_bottom.pack(fill=X, expand=YES)

frame_results = Frame(top)
frame_results.pack(fill=X, expand=YES)

Label(frame_inputs_top,
      text="Sentence splitting", font=DEFAULT_FONT).pack(side=TOP)

Label(frame_inputs_bottom,
      text="Enter your string:", font=DEFAULT_FONT).pack(side=LEFT)
str_input = Entry(frame_inputs_bottom, font=DEFAULT_FONT)
str_input.pack(side=RIGHT, fill=BOTH, expand=YES)

Button(frame_results, text="Obtain", font=DEFAULT_FONT,
       command=split_event).pack(side=TOP)

list_bar = Scrollbar(frame_results, orient=VERTICAL)

list_out = Listbox(frame_results, font=DEFAULT_FONT, yscrollcommand=list_bar.set)
list_out.pack(side=LEFT, fill=BOTH, expand=YES)

list_bar.configure(command=list_out.yview)
list_bar.pack(side=RIGHT, fill=Y)

top.mainloop()
