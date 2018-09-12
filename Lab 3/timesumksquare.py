import time
import math
import statistics

def selectionsort(L):
    start = time.time()
    for i in range(len(L)):
        smallest = L[0]
        for x in range(len(L) - 1):
            if smallest > L[x + 1]:
                temp = L[x + 1]
                L[x + 1] = L[x]
                L[x] = temp
    end = time.time()
    return L, end - start

def sumksquare2(k):
    start = time.time()
    total = ((k * (k + 1)) * ((2 * k) + 1)) / 6
    end = time.time()
    return total, end - start


def sumksquare(k):
    start = time.time()
    total = 0
    for i in range(0, k + 1):
        total += i ** 2
    end = time.time()
    return total, end - start