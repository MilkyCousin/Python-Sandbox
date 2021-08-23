import random

def is_increasing(x):
    for i in range(1,len(x)):
        if x[i-1] > x[i]:
            return False
    return True

def bogo_sort(x):
    a = x.copy()
    while not is_increasing(a):
        a = random.shuffle(a)
    return a
