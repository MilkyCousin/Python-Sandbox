def LinearSearch(x, q):
    l = len(x)
    for i in range(l):
        if x[i] == q:
            return i
    return None