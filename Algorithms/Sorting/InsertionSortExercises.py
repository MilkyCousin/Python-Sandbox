from InsertionSort import insertion_sort_simplified

# 2.1-1

"""
Using Figure 2.2 as a model, illustrate the operation of INSERTION-SORT on the
array A = {31; 41; 59; 26; 41; 58}.
"""

A = [31, 41, 59, 26, 41, 58]
B = insertion_sort_simplified(A)

print(B)

# 2.1-2

"""
Rewrite the INSERTION-SORT procedure to sort into nonincreasing instead of nondecreasing order.
"""

def insertion_sort_decreasing(x):
    a = x.copy()
    l = len(a)
    for i in range(1, l):
        c = a[i]
        k = i - 1
        while a[k] < c:
            a[k + 1] = a[k]
            k -= 1
            if k == -1: break
        a[k + 1] = c
    return a

print(insertion_sort_decreasing(A))

# 2.1-3

"""
Consider the searching problem:
Input: A sequence of n numbers A = {a1; a2; ... ; an} and a value q
Output: An index i such that q = A[i] or the special value NIL if q does not
appear in A.
Write pseudocode for linear search, which scans through the sequence, looking
for q. Using a loop invariant, prove that your algorithm is correct. Make sure that
your loop invariant fulfills the three necessary properties.
"""

def linear_search(x, q):
    l = len(x)
    for i in range(l):
        if x[i] == q:
            return i
    return None

print(linear_search(A, 59))
print(linear_search(A, 111))

# 2.1-4

"""
Consider the problem of adding two n-bit binary integers, stored in two n-element
arrays A and B. The sum of the two integers should be stored in binary form in
an (n + 1)-element array C. State the problem formally and write pseudocode for
adding the two integers.
"""

"""
Input:
A = [a_1, ..., a_n], B = [b_1, ..., b_n]
a_j, b_j \in {0,1}
0 + 0 = 0, 0 + 1 = 1, 1 + 1 = 0 (1)
Output
C = [c_1, ..., c_{n+1}]
"""

def xor(x,y):
    return bool((not x and y) or (x and not y))

def binary_addition(a,b):
    assert len(a) == len(b)

    #return c[::-1]

print(binary_addition([0,0],[0,0])) # [0,0,0]
print(binary_addition([0,0],[0,1])) # [0,0,1]
print(binary_addition([0,1],[0,1])) # [0,1,0]
print(binary_addition([1,1],[0,1])) # [1,0,0]
print(binary_addition([1,1],[1,1])) # [1,1,0]