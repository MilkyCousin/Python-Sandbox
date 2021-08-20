def selection_sort(x):
    a = x.copy()
    l = len(a)
    for i in range(l-1):
        m = i
        for j in range(i+1,l):
            if a[j] < a[m]:
                m = j
        a[i],a[m] = a[m],a[i]
    return a

if __name__ == "__main__":
    A = [31, 41, 59, 26, 41, 58]
    print(selection_sort(A))

    B = [31]
    print(selection_sort(B))

    C = [31, 30]
    print(selection_sort(C))