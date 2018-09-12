import random


def quicksort(L, left=0, right=None):
    if right is None:
        right = len(L)

    if right - left > 1:
        # Divide!
        mid, cost_p = partition(L, left, right)

        # Conquer!
        cost_l = quicksort(L, left, mid)
        cost_r = quicksort(L, mid + 1, right)
        # Combine!
        # Nothing to do!
    else:
        return 1
    return cost_p + cost_l + cost_r

def partition(L, left, right):
    pivot = right - 1
    i = left  # index in left half
    j = pivot - 1  # index in right half

    while i <= j:
        while L[i] <= L[pivot] and i <= j:
            i += 1
        while L[i] >= L[pivot] and i <= j:
            while L[j] >= L[pivot] and i <= j:
                j -= 1
            if i < j:
                L[i], L[j] = L[j], L[i]
    # Put the pivot in place
    L[pivot], L[i] = L[i], L[pivot]
    return i, right - left


### Reversely sorted lists
print("Sorting reversely sorted lists...")
costs = []
for l in range(10):
    L = [i for i in range(2 ** l, 0, -1)]
    cost = quicksort(L)
    print(cost)
    costs.append(cost)

print("Scaling factors:")
for k in range(len(costs) - 1):
    print(costs[k + 1] / costs[k])

### Already sorted lists
print("Sorting already sorted lists...")
costs = []
for l in range(10):
    L = [i for i in range(2 ** l)]
    cost = quicksort(L)
    print(cost)
    costs.append(cost)

print("Scaling factors:")
for k in range(len(costs) - 1):
    print(costs[k + 1] / costs[k])

random.seed(15)
### Random cases
print("Sorting random lists...")
costs = []
for l in range(10):
    cost = 0
    ## Repeating 100 times
    for k in range(100):
        L = [random.randrange(i) for i in range(2 ** l, 0, -1)]
        # print(L)
        cost += quicksort(L)
    print(cost / 100)
    costs.append(cost / 100)

print("Scaling factors:")
for k in range(len(costs) - 1):
    print(costs[k + 1] / costs[k])
