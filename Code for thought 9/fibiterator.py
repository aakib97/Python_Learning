## Code for thought #9
## We need to implement an iterator to display Fib numbers that are less than
## a preset maximum value.

## First, we need to add one line of code to complete the implementation of the
## iterator. Submit your code and check whether you pass the test case.

## Second, try to move the follow initilzation to __init__(self, max) method,
## and see whether
## print([2*x for x in fib]) 
## still works. Refelect on why it does not work reason any more.

## Correct this code again and we should already got a good understanding of
## where to set the initial values of an iterator.


class Fib:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a = self.b
        self.b = fib + self.a
        return fib


fib = Fib(1000)
for f in fib:
    print(f)

print([2 * x for x in fib])
