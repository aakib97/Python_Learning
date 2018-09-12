def rotationcount(L):
    def rotation(L, left=0, right=None):
        if right is None: right = len(L1) - 1
        if (right - left) < 1:
            return 0
        median = (right + left) // 2
        if L[left] > L[median] and L[median] < L[median - 1]:
            return median
        elif L[right] < L[median] and L[median] > L[median + 1]:
            return median
        elif L[right] < L[median] < L[median + 1]:
            return rotation(L, median)
        elif L[left] > L[median] < L[median - 1]:
            return rotation(L, left, median)
    return rotation(L, 0)


L1 = [6, 7, 8, 11, 12, 5]
print(rotationcount(L1))
