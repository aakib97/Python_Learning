### Run the current code and try to understand the printed results
### You can see that the algorithm actually see the number we are looking for
### very early but the algorithm does not stop
### add one line of code to the function bs to avoid the above senario

visited = []
def bs(L, item, left = 0, right = None):
    if right is None: right = len(L)
    if right - left == 0: return False
    if right - left == 1: return L[left] == item
    median = (right + left)//2
    visited.append(L[median])
    if item in visited: return True
    if item < L[median]:
        return bs(L, item, left, median)
    else:
        return bs(L, item, median, right)


L = [i for i in range(1024)]

print(bs(L, 512))
print(visited)
visited = []
