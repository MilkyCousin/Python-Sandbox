def is_increasing(x):
    for i in range(1,len(x)):
        if x[i-1] > x[i]:
            return False
    return True