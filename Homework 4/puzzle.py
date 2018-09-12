## Solves puzzle recursivly
## L is a list representing the puzzle #s
## i is the current index of the marker in L
## visited is a Set of visited indices
def puzzle(L, i, visited):
    if visited is None: visited = set()
    if i > len(L) - 1:
        return False
    if L[i] == 0 and i != len(L) - 1:
        return False
    if i == len(L) - 1:
        return True
    elif i < 0:
        return False
    elif i in visited:
        return False
    elif i == 0:
        visited.add(i)
        puzzle(L, L[i], visited)
    if puzzle(L, i + L[i], visited):
        return True
    elif puzzle(L, i - L[i], visited):
        return True
    else:
        return False
