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
        l -= 1
    return a


def BogoSort(x):
    a = x.copy()
    while not is_increasing(a):
        random.shuffle(a)
    return a


def MergeSort(x):
    a = x.copy()
    if not a or len(a) == 1:
        return a
    else:
        l = len(a)//2
        return to_merge(MergeSort(a[:l]), MergeSort(a[l:]))


def QuickSort(x):
    a = x.copy()
