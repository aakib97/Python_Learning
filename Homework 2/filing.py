
def leftmostfiling(L):          # L: list of document IDs acquired from the pile
    M = [x for x in range(20)]  # initialize a pile of 20 documents
    count = 0                   # sum of total number of documents passed before finding each document in L
    for l in L:
        if l in M:
            count += M.index(l)
            M.remove(l)
            M.insert(0, l)
    return count

def rightmostfiling(L):
    M = [x for x in range(20)]
    count = 0
    for l in L:
        if l in M:
            count += M.index(l)
            M.remove(l)
            M.insert(int((len(M))) + 1, l)
    return count

def fixedfiling(L):
    M = [x for x in range(20)]
    count = 0
    for l in L:
        if l in M:
            count += 2*(M.index(l))
            temp_pos = M.index(l)
            M.remove(l)
            M.insert(temp_pos, l)
    return count



### Do not modify anything below, for testing purposes only.
# Random requests
print("Random request")
L = [int(line) for line in open('data.txt')]

print("Cost for leftmost filing:", leftmostfiling(L))
print("Cost for fixed filing :", fixedfiling(L))
print("Cost for rightmost filing :", rightmostfiling(L))

# Always request first item
print("Always request first item")
L = [0]*100000
print("Cost for leftmost filing :", leftmostfiling(L))
print("Cost for fixed filing :", fixedfiling(L))
print("Cost for rightmost filing :", rightmostfiling(L))

# Always request last item
print("Always request last item")
L = [19]*100000
print("Cost for leftmost filing :", leftmostfiling(L))
print("Cost for fixed filing :", fixedfiling(L))
print("Cost for rightmost filing :", rightmostfiling(L))

# Repeated requests

print("Repeated requests #1")
L = [x for x in range(20)]*5000
print("Cost for leftmost filing :", leftmostfiling(L))
print("Cost for fixed filing :", fixedfiling(L))
print("Cost for rightmost filing :", rightmostfiling(L))

print("Repeated requests #2")
L = [x for x in range(10)]*10000
print("Cost for leftmost filing :", leftmostfiling(L))
print("Cost for fixed filing :", fixedfiling(L))
print("Cost for rightmost filing :", rightmostfiling(L))

print("Repeated requests #3")
L = [x + 10 for x in range(10)]*10000
print("Cost for leftmost filing :", leftmostfiling(L))
print("Cost for fixed filing :", fixedfiling(L))
print("Cost for rightmost filing :", rightmostfiling(L))
