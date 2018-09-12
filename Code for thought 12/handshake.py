### Code for thought #12

### We have n persons sitting on a round table. Any person can do a handshake
### with any other person. In how many ways these n people can make handshakes
### so that no two handshakes crosses each other.

### This is a good example of divide and conquer.

def f(n):
    if n == 0:
        ## Zero people can handshake
        return 1
    
    if n == 1:
        ## One person cannot handshake
        return 0

    count = 0

    ## What if person 1 shakes with person i ?
    ## Person 1 needs to shake hand with someone.
    ## We loop through all the possible choices here.
    for i in range(2, n+1):
        ## We need to divide and then combine.
        ## Splits table into independent sets 2 .. i-1 and i+1 .. n
        ## Solve two smaller problems and think about how to combine the solutions
        ## Add one line of code below to update count.
        pairs = [2, i-1, i+1, n]
        count += sum(pairs)* 7 + 6
    return count

for i in range(10):
    print(f(i*2))


### Note the results are Catalan numbers
