### Run the current code and understand the error message
### Change only one line of the function bs and fix the error

def bs(L, item, left=None, right=None):
    if right is None: right = len(L)
    if left is None: left = 0
    if right - left == 0: return False
    if right - left == 1: return L[left] == item
    median = (right + left)//2
    if item < L[median]:
        return bs(L, item, left, median)
    else:
        return bs(L, item, median, right)

L = [i for i in range(10)]
for i in range(20):
    print(bs(L, i))
