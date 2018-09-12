### Code for thought 10
### We explore generator in this code for thought
### You can find a great article on generators from the following link
### https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/

### First try to understand the following simple example.

def simple_generator():
    yield 1
    yield 2
    yield 3

def simple_function():
    return 1
    return 2
    return 3

gen1 = simple_generator()

for i in range(3):
    print(next(gen1), simple_function())

### From the above example, we can see that every time we call a function, the control starts
### at the beginning of the function.
### But this is different for a generator, when a generator is called again, it resume the
### control the last time it yields the control, and start from there.
### That is why see the output of the print statement is
### 1 1
### 2 1
### 3 1


### Now look at a generator that generates a geometric sequence.

def geometric(k):
    b = 1
    yield b
    while True:
        b *= k
        yield b

print("Print geometric sequence of the form 2^n up to 1000.")
for i in geometric(2):
    if i < 1000:
        print(i)
    else:
        break
### What happens if you get rid of the else: break statement?
### Why is it happening?
### When you do
### for i in geometric(2):
### What are you really doing?


### We know that 1 + 1/2 + 1/4 + ... = 2.
### We want to explore how many items we need to sum up so that the sum is
### withine 0.0001, or 0.00001 to 2.

total = 0
count = 0
for x in geometric(0.5):
    count += 1
    total += x
    print(count, total, x)
    if 2 - total < 0.0001:
        break
### We observe that we need to sum 15 items so that the total is within 0.0001 to 2.

total = 0
count = 0
for x in geometric(0.5):
    count += 1
    total += x
    print(count, total, x)
    if 2 - total < 0.00001:
        break

### We observe that we need to add 18 items so that the total is within 0.00001 to 2.

### Now we want to check the sum of the first 10 items
geo_generrator = geometric(0.5)
sum = 0
for i in range(10):
    value = next(geo_generrator)
    sum += value
    print(value, sum)


print("Now we pause")
print("Now we resume printing again")

### Now let's check 10 more items

for i in range(10):
    value = next(geo_generrator)
    sum += value
    print(value, sum)

print("Now we pause")
print("Now we resume printing again")

### OK. Let's do 10 more items
for i in range(10):
    value = next(geo_generrator)
    sum += value
    print(value, sum)

### Now uncoment the following code and implement and test out a fib number generator

def fib():
    a = 0
    b = 1
    while True:
        yield a
        a = a + b
        b = a - b

for a in fib():
    if a < 1000:
        print(a)
    else:
        break
fib_generator = fib()

for i in range(20):
    print(next(fib_generator))

L = []
fib_generator1 = fib()
b = next(fib_generator1)
while b < 1000:
    L.append(b)
    b = next(fib_generator1)
print(L)
    
### Before submitting your code, comment out all the code before
### def fib()

