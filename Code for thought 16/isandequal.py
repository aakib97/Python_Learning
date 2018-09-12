## Code for thought #16
## Run the code and you will notice an ValueError
## Use try statement and exception handling to fix the error
## Once you code can run, you should notice that there is a error in the printout
## Try to fix that error.
## Hint
## is and ==
## is not the same thing.


## Read the following and make sure you understand.

##is will return True if two variables point to the same object, == if the objects referred to by the variables are equal.
##
##>>> a = [1, 2, 3]
##>>> b = a
##>>> b is a 
##True
##>>> b == a
##True
##>>> b = a[:]
##>>> b is a
##False
##>>> b == a
##True

class Person:
    def __init__(self, name, ssn):
        self._name = name
        self._ssn = ssn

    def __eq__(self, other):
        return isinstance(other, Person) and self._ssn is other._ssn

    def __hash__(self):
        return hash(self._ssn)

    def __str__(self):
        return str('(' + self._name) + ' : ' + str(self._ssn) + ')'


class Prison:
    def __init__(self):
        self._cells = [[] for i in range(10)]

    def add(self, person):
        self._cells[hash(person) % 10].append(person)

    def remove(self, person):
        try:
            self._cells[hash(person) % 10].remove(person)
        except ValueError:
            return 0

    def __contains__(self, person):
        for cell in self._cells:
            for p in cell:
                if person == p:
                    return True
        return False


def check(p, prison):
    if p in prison:
        print(p, "in prison.")
    else:
        print(p, "not in prison.")


p = Person('Behind Bars', 123456789)
q = Person('Fake Name', 123456789)
r = Person('Good Guy', 987654321)
prison = Prison()
prison.add(p)

check(p, prison)
check(q, prison)
check(r, prison)

prison.remove(r)
prison.remove(q)
check(p, prison)
check(q, prison)
check(r, prison)
