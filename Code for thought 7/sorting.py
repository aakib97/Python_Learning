## Code for thought 07
## Change the following sorting algorithms so that each algorithm returns
## the number of swaps between the list items,
## the number of comparisons between list items,
## and the sum of these two operations in the sorting algorithm

def bubblesort(L):
    count_s = count_c = 0
    keepgoing = True
    while keepgoing:
        keepgoing = False
        for i in range(len(L) - 1):
            count_c +=1
            if L[i] > L[i + 1]:
                count_s +=1
                L[i], L[i + 1] = L[i + 1], L[i]
                keepgoing = True
    return count_s, count_c, count_s + count_c


def selectionsort(L):
    count_s = count_c = 0
    n = len(L)
    for i in range(n - 1):
        max_index = 0
        for index in range(n - i):
            count_c += 1
            if L[index] > L[max_index]:
                max_index = index
        L[n - i - 1], L[max_index] = L[max_index], L[n - i - 1]
        count_s +=1
    return count_s, count_c, count_s + count_c


def insertionsort(L):
    count_s = count_c = 0
    n = len(L)
    for i in range(n):
        j = n - i - 1
        while j < n - 1 and L[j] > L[j + 1]:
            L[j], L[j + 1] = L[j + 1], L[j]
            count_s +=1
            j += 1
        count_c += 1
    return count_s, count_c, count_s + count_c
