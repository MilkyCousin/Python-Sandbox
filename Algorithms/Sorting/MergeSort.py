def combine(x,y):
    a = x.copy()
    b = y.copy()
    c = []
    while a and b:
        c.append(a.pop(0) if a[0] < b[0] else b.pop(0))
    c.extend(a)
    c.extend(b)
    return c

def to_merge(subset_left, subset_right):
    assert len(subset_left) == len(subset_right)
    l = len(subset_left)
    if l == 1:
        return combine(subset_left, subset_right)
    else:
        s = l//2
        return combine(to_merge(subset_left[:s], subset_left[s:]), to_merge(subset_right[:s], subset_right[s:]))

def merge_retarded(x):
    a = x.copy()
    l = len(a) # assuming l = 2^k, gg
    s = l//2
    return to_merge(a[:s], a[s:])

def split_array(x):
    a = x.copy()
    l = len(a)
    if not l%2:
        s = l//2
        return [a[:s], a[s:]]
    else:
        s = (l - 1) // 2
        return [a[:s], a[s:-1], [a[-1]]]

def merge_sort_adequate(x):
    ...
