# T20.1 Сформулювати гіпотези щодо наявності та значень границь послідовностей {an}.
# Для цього побудувати масиви numpy зі значеннями n та an. Припустити, що границя
# послідовності {an} дорівнює b. Для заданого малого ε > 0 перевірити, що у масиві an,
# починаючи з деякого k, для m > k |am - b| < ε.
# Графічно відобразити елементи послідовності, а також пряму y = b. Побудувати графік
# полоси (b - ε, b + ε) та показати, що усі елементи an, при n>k, потрапляють у цю полосу.
# Самостійно підібрати масштаб осей для ілюстрації наявності границі.
#        sqrt(n*(n^4+1)) - sqrt((n^3-1)*(n^2+2))
# an := -----------------------------------------, n = 1,2,...
#                        sqrt(n)

import numpy as np
import matplotlib.pyplot as plt


def sequence(m):
    return ((m * (m**4+1))**0.5 - ((m**3-1) * (m**2+2))**0.5) / (m**0.5)


b = -1
n = int(input("Enter the number of elements of {an}:\n"))
eps = float(input("Enter the value for epsilon (accuracy):\n"))

n_seq = np.arange(1, n+1, dtype=float)
n_lin = np.linspace(1, n+1)

seq = sequence(n_seq)

plt.title("Hypothesis on limit with n = %i, eps = %g" % (n, eps))
plt.scatter(n_seq, seq, color="black", s=0.75, label="an")

plt.plot(n_lin, b*np.ones_like(n_lin), color="blue", label="b := lim{an} = %g" % b)
plt.plot(n_lin, (b-eps)*np.ones_like(n_lin),
         color="red", linestyle="-", label="b +/- eps")
plt.plot(n_lin, (b+eps)*np.ones_like(n_lin),
         color="red", linestyle="-")

b = np.abs(seq - b) < eps
if np.any(b):
    k = np.argmax(b)
    y_lim_current = plt.gca().get_ylim()
    plt.vlines(k, y_lim_current[0], y_lim_current[1],
               color="green", linestyle="--", label="k: for all m > k: |am - b| < eps")
    print("The value of k obtained, k = %i" % k)
else:
    print("Cannot obtain the value of k for given n and eps")

plt.legend()
plt.savefig("%s.png" % input("Enter the name of image to save:\n"))
