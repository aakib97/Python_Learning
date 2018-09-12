### First read the following function that caculates the Fib numbers
def fib(k):
    if k in {0, 1}:
        return k
    return fib(k - 1) + fib(k - 2)


for i in range(20):
    print(i, fib(i))


### The above function correctly calculates the Fib numbers as shown
### by the print statements above

### We are interested in how many function calls are made to calculate
### each Fib number
### We modify the above function to accomplish that

### Try to undertand the following code and see how the above goal
### is accomplished


def fib1(k):
    if k == 0:
        return 0, 1
    if k == 1:
        return 1, 1
    u = fib1(k - 1)
    v = fib1(k - 2)
    return u[0] + v[0], u[1] + v[1] + 1


for i in range(20):
    print(i, fib1(i))


### From the printout above, you should see that the number of function calls
### to calculate the Fib numbers are staggering
### Try to visualize on paper how each of these function call is made

### From the print out can you convince yourself that the number of function
### calls are exponential in terms of k?


### In fact, we can calculate Fib numbers using way less function calls
### We will now implement a goodfib function so that the number of function
### calls are linear
### In the return statement, the last parameter is the number of calls
### You can guess the meaning of the first two parameters from our class notes
### and slides

def goodfib(k):
    if k == 0:
        return 0, 0, 1
    if k == 1:
        return 1, 0, 1
    u = goodfib(k - 1)
    return u[0] + u[1], u[0], k


for i in range(20):
    print(i, goodfib(i))