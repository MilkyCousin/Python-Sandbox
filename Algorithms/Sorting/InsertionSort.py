def insertion_sort(x):
    a = x.copy()
    l = len(a)
    for i in range(1,l):
        c = a[i]
        k = i
        for j1 in range(i-1,-1,-1):
            if a[j1] <= c:
                break
            k = j1
        for j2 in range(i, k, -1):
            a[j2] = a[j2 - 1]
        a[k] = c
    return a

def insertion_sort_simplified(x):
    a = x.copy()
    l = len(a)
    for i in range(1,l):
        c = a[i]
        k = i-1
        while a[k] > c:
            a[k+1] = a[k]
            k -= 1
            if k == -1: break
        a[k+1] = c
    return a

if __name__ == "__main__":
    import random

    random.seed(0)

    N = 10
    A = [random.randint(0, 100) for i in range(N)]

    print(A)
    print(insertion_sort(A))
    print(insertion_sort_simplified(A))