from Utility.utilities import *


def InsertionSort(x, decreasing=False):
    a = x.copy()
    l = len(a)
    s = (-1)**(int(decreasing))
    for i in range(1, l):
        c = a[i]
        k = i - 1
        while s * (a[k] - c) > 0:
            a[k + 1] = a[k]
            k -= 1
            if k == -1:
                break
        a[k + 1] = c
    return a


def SelectionSort(x, decreasing=False):
    a = x.copy()
    l = len(a)
    s = (-1)**(int(decreasing))
    for i in range(l-1):
        m = i
        for j in range(i+1, l):
            if s * (a[j] - a[m]) < 0:
                m = j
        a[i], a[m] = a[m], a[i]
    return a


def BubbleSort(x):
    a = x.copy()
    l = len(a)
    while not is_increasing(a):
        for i in range(1,l):
            if a[i-1] > a[i]:
                a[i-1], a[i] = a[i], a[i-1]
    return a


def to_merge(a, b):
    c = []
    while a and b:
        c.append(a.pop(0) if a[0] < b[0] else b.pop(0))
    c.extend(a)
    c.extend(b)
    return c


def MergeSort(x):
    a = x.copy()
    if not a or len(a) == 1:
        return a
    else:
        l = len(a)//2
        return to_merge(MergeSort(a[:l]), MergeSort(a[l:]))
