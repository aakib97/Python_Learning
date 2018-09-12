import time

cost_A = 0
cost_B = 0
cost_m = 0


def mergesort(L):
    # Base Casee
    if len(L) < 2:
        return 1

    # Divide!
    mid = len(L) // 2
    A = L[:mid]
    B = L[mid:]


    # Conquer!
    cost_A = mergesort(A)
    cost_B = mergesort(B)

    # Combine!
    cost_m = merge(A, B, L)

    return cost_A + cost_B + cost_m + 1


def merge(A, B, L):
    i = 0  # index into A
    j = 0  # index into B
    k = 0  # index into L
    global cost_m
    cost_m += 1
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            L[k] = A[i]
            i += 1
        else:
            L[k] = B[j]
            j += 1
        k += 1
    L[k:] = A[i:] + B[j:]
    return len(L)
