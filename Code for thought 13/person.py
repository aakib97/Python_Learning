## Code for thought #13

## In this code for thought we explore how to define a class that is hashable
## so that we can use the objects of the class in sets and dictionaries.
## After this excercise, we should get a better understanding of what kind of
## objects can be put into a set and what kind of objects can be used as keys
## in a dictionary.

## An object is hashable if it has a hash value which never changes during its
## lifetime (it needs a __hash__() method), and can be compared to other
## objects (it needs an __eq__() method). Hashable objects which compare equal
## must have the same hash value.

## Hashability makes an object usable as a dictionary key and a set member,
## because these data structures use the hash value internally.

## All of Python’s immutable built-in objects are hashable; mutable containers
## (such as lists or dictionaries) are not. Objects which are instances of
## user-defined classes are hashable by default. They all compare unequal
## (except with themselves), and their hash value is derived from their id().

## Read and understand the following code and then predict the outputs. 
## Once you think you understand the code, run the code and see whether the
## outputs are as you expected.

class Person:
    def __init__(self, name, ssn):
        self._name = name
        self._ssn = ssn

    def __eq__(self, other):
        return isinstance(other, Person) and self._ssn == other._ssn

    def __hash__(self):
        # use the hashcode of self.ssn since that is used
        # for equality checks as well
        return hash(self._ssn)

    def __str__(self):
        return str('(' + self._name) + ' : ' + str(self._ssn) + ')'

p = Person('Foo Bar', 123456789)
q = Person('Fake Name', 123456789)
s = set()
s.add(p)
s.add(q)

print("All persons in the set:")
for person in s:
    print(person)

print("p == q is", p == q)
    
d = {}
d[p] = 1
print("d[p], d[q] = ", d[p], "," ,d[q])
d[q] += 1
print("d[p], d[q] = ", d[p], "," ,d[q])

## Now we uncomment the following code and finish this excercise
## First we randomly geneate a list of persons
import random
random.seed(15)
L = []
for i in range(20):
    p = Person(str(random.randrange(20)), random.randrange(20))
    L.append(p)


## Use a dictionary d to count the number of times each person appeared
## in list L

d = {}
for p in L:
## Add one line of code below

print("Number of persons:", len(d))
print("Frequency of appearence:")
for p in d:
    print(p, d[p])
