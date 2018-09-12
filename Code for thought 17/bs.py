### In this excercise, we will change a binary search algorithm to solve the
### problem #2 in the second midterm


### Consider a list of distinct numbers sorted in increasing order. The list
### has been rotated (anit-clockwise) k number of times. Given such an list,
### find the value of k.

### Examples:
### Input: L = [15, 18, 2, 3, 6, 12]. Output: 2
### Input: L = [7, 9, 11, 12, 5]. Output: 4
### Input: L = [7, 9, 11, 12, 15]. Output: 0.


### Copy the code from bs to rotatecount and make neccesary changes to solve the
### above problem.

### Make as less change as possible. This will help you understand how to convert
### a problem to a solved problem, and take advantage of existing code that is
### already well tested.

def bs(L, item, left=0, right=None):
    if right is None: right = len(L)
    if right - left == 0: return False
    if right - left == 1: return L[left] == item
    median = (right + left) // 2
    if L[median] == item: return True
    if item < L[median]:
        return bs(L, item, left, median)
    else:
        return bs(L, item, median, right)


def rotatecount(L):
    count = 0
    for i in L:
        if not bs(L, i):
            if L.index(i) == 0:
                count = L.index(i) + 1
            else:
                count = L.index(i)
    return count


L = [1, 2, 3, 4, 5, 6]
print(L)
print(rotatecount(L))
L = [7, 9, 11, 12, 5]
print(L)
print(rotatecount(L))
L = [15, 18, 2, 3, 6, 12, 14]
print(L)
print(rotatecount(L))
L = [10, 1, 2, 3, 4]
print(L)
print(rotatecount(L))
L = [1]
print(L)
print(rotatecount(L))
L = [2, 1]
print(L)
print(rotatecount(L))
L = [2, 3, 1]
print(L)
print(rotatecount(L))
L = [1, 2, 3]
print(L)
print(rotatecount(L))
L = [3, 1, 2]
print(L)
print(rotatecount(L))
L = [2, 3, 4, 1]
print(L)
print(rotatecount(L))
L = [3, 4, 1, 2]
print(L)
print(rotatecount(L))
L = [5, 6, 1, 2, 3, 4]
print(L)
print(rotatecount(L))
L = [3, 1, 2]
print(L)
print(rotatecount(L))
L = [2, 3, 1]
print(L)
print(rotatecount(L))
L = []
print(L)
print(rotatecount(L))
