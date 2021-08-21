# Т20.13 Задані координати n точок на площині (x1,y1),...,(xn,yn). Знайти номери
# двох точок, відстань між якими найбільша (вважати, що така пара точок єдина), та саму
# відстань.


import numpy as np


def dist(x1, x2, y1, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def max_dist(x, y):
    assert len(x) == len(y)
    idx_i, idx_j = np.meshgrid(np.arange(len(x)), np.arange(len(y)))
    sq_dist_matrix = dist(x[idx_i], x[idx_j], y[idx_i], y[idx_j])
    return sq_dist_matrix


n = int(input("Enter the number of points:\n"))
X = []
Y = []

for i in range(1, n+1):
    print("Point #%i:" % i)
    X.append(float(input("Enter the value of x-coordinate:\n")))
    Y.append(float(input("Enter the value of y-coordinate:\n")))

X = np.array(X)
Y = np.array(Y)

m = max_dist(X, Y)
mx = np.max(m)
m_loc = np.where(m == mx)[0]  # i don't like this, actually

print("Maximum distance:\n" + str(mx ** 0.5))
print("Chosen pair of points: " + str(m_loc))
print(np.vstack((X, Y)).T[m_loc])
