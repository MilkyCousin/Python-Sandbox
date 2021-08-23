import random

def is_increasing(x):
    for i in range(1,len(x)):
        if x[i-1] > x[i]:
            return False
    return True


def to_merge(a, b):
    c = []
    while a and b:
        c.append(a.pop(0) if a[0] < b[0] else b.pop(0))
    c.extend(a)
    c.extend(b)
    return c
