### The following function should return True or False based on the happiness of the input.
### Please note the type of the input parameter variable, number, should be string.
numb = []

def happy(number):
    numlist = list(number)

    def addsquare(l):
        term = 0
        for x in range(len(l)):
            term += int(l[x]) ** 2

        return term

    squaresum = addsquare(numlist)
    if squaresum == 1:
        del numb[:]
        return True
    elif squaresum in numb:
        del numb[:]
        return False
    else:
        numb.append(squaresum)
        return happy(str(squaresum))


### Do not modify anything below, for testing purposes only.
n = 0
for i in range(1000):
    s = str(i+1)
    if happy(s):
        n += 1;
        print(n, ':', s)
