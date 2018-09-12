### Code for thought #2
### Use recursion to reverse a list
### Finish the code for function reverselist


def reverselist(L, low, high):
    if low < high:
        L[low], L[high] = L[high], L[low]
        reverselist(L, low+1, high - 1)
    return L

L = [ i for i in range(10)]
print("Before revese:")
print(L)
print("After reverse:")
print(reverselist(L, 0, len(L)-1))

