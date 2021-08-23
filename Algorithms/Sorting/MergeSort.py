def to_merge(a, b):
    c = []
    while a and b:
        c.append(a.pop(0) if a[0] < b[0] else b.pop(0))
    c.extend(a)
    c.extend(b)
    return c


def merge_sort(x):
    a = x.copy()
    if not a or len(a) == 1:
        return a
    else:
        l = len(a)//2
        return to_merge(merge_sort(a[:l]), merge_sort(a[l:]))
