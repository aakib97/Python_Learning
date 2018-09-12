### This function uses the Gregory Leibniz series to calculate Pi with n terms, and returns the value of the estimated Pi.
def GregoryLeibniz(n):
    result = 0
    for x in range(n):
        if x == 0:
            result = (((-1) ** x) * (4 / ((2 * x) + 1)))
        else:
            result = result + (((-1) ** x) * (4 / ((2 * x) + 1))) 
    return result


### This function uses the Nilakantha series to calculate Pi with n terms, and returns the value of the estimated Pi.
def Nilakantha(n):
    result = 0
    offset = 3
    for x in range(n):
        if x == 0:
            result = offset + (((-1) ** x) * (4 / ((2 * (x + 1)) * ((2 * (x + 1)) + 1) * ((2 * (x + 1)) + 2))))
        else:
            result = result + (((-1) ** x) * (4 / ((2 * (x + 1)) * ((2 * (x + 1)) + 1) * ((2 * (x + 1)) + 2))))
    return result


### You do not need to modify this piece of code. It will call the two functions above iteratively.
n = 100
for i in range(n):
    print(i+1, GregoryLeibniz(i+1), Nilakantha(i+1))


### In this piece of code, we print the minimum number of terms required in order to approximate pi within an accuracy of 0.001 by using Gregory Leibniz series, together with the approximated value of pi.
pi = 3.1415927      # We assume that the true value of pi is 3.1415927
accuracy = 0.001    # Approximation accuracy that we need to achieve
i = 0               # Number of terms included in the pi calculation 
diff = 1            # Difference between the approximation and the ture value of pi, initialized to be 1. We will find the corresponding i when diff is smaller than 0.001
result = 0          # Approximation value of pi, initialized to be 0

while diff > accuracy:
    i = i + 1
    diff = abs(GregoryLeibniz(i) - pi)
result = GregoryLeibniz(i)

print("GregoryLeibniz", i, result) 


### In this piece of code, we print the minimum number of terms required in order to approximate pi within an accuracy of 0.001 by using Nilakantha series, together with the approximated value of pi.
i = 0
diff = 1
while diff > accuracy:
    i = i + 1
    diff = abs(Nilakantha(i) - pi) 
result = Nilakantha(i)

print("Nilakantha", i, result)
