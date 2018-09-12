## Code for thought #6
## The following code implemented the class SimpleSortedList and BSSortedList
## where BSSortedList improves the performance of the __contains__ method.

## One thing that is not very convinent when I use the this BSSortedList class is
## that I cannot use a list to initialize a sorted list. I have to initilize a
## sorted list to be a empty list and then add items to it.

## To make improvement to this, we define a class called GoodBSSortedList based on
## BSSortedList and change the __init__ method.

## Finish the initializer of this new class so that the code in the main part works
## as intended.

class SimpleSortedList:
    def __init__(self):
        self._L = []

    def add(self, item):
        self._L.append(item)
        self._L.sort()

    def remove(self, item):
        self._L.remove(item)

    def __getitem__(self, index):
        return self._L[index]

    def __contains__(self, item):
        return item in self._L

    def __len__(self):
        return len(self._L)

    def __iter__(self):
        return iter(self._L)

class BSSortedList(SimpleSortedList):
    def __contains__(self, item):
        left, right = 0, len(self._L)
        while right - left > 1:
            median = (right + left)//2
            if item < self._L[median]:
                right = median
            else:
                left = median
        return right > left and self._L[left] == item

class GoodBSSortedList(BSSortedList):
    def __init__(self, L = None):
        self._L = []
        for i in L:
            self.add(i)



print("Printout for BSSortedList:")
L = BSSortedList()
for l in [i for i in range(10, 0, -1)]:
    L.add(l)

for l in L:
    print(l)

print("Printout for GoodBSSortedList:")
L = GoodBSSortedList([i for i in range(10, 0, -1)])
for l in L:
    print(l)
