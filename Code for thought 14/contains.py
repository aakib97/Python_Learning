## Code for thought 14

## In this excercise, we go over an implementation of ListMapping
## When you run the code, there will be an error.
## Find out what causes the error and fix the error.
## When you are done with the excercise, you should have already got a good
## understanding of the __cotains__ method and how the method is called.
## You should also already got a good understanding of excpetions and how to
## handle exceptions.
## Also, think through why the statement
## print(map1)
## can work even though we do not see __str__ method implemented in the class
## ListMapping. This will help you understand class inheritance.

## Also note a few of the methods in class Mapping is not implemented. Think
## what is the reason for that.


class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) + ": " + str(self.value)


class Mapping:
    # Child class needs to implement this!
    def get(self, key):
        raise NotImplementedError

    # Child class needs to implement this!
    def put(self, key, value):
        raise NotImplementedError

    # Child class needs to implement this!
    def __len__(self):
        raise NotImplementedError

    # Child class needs to implement this!
    def _entryiter(self):
        raise NotImplementedError

    def __iter__(self):
        return (e.key for e in self._entryiter())

    def values(self):
        return (e.value for e in self._entryiter())

    def items(self):
        return ((e.key, e.value) for e in self._entryiter())

    def __contains__(self, key):
        return self.get(key)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __str__(self):
        return "{%s}" % (", ".join([str(e) for e in self._entryiter()]))


class ListMapping(Mapping):
    def __init__(self):
        self._entries = []

    def put(self, key, value):
        e = self._entry(key)
        if e is not None:
            e.value = value
        else:
            self._entries.append(Entry(key, value))

    def get(self, key):
        e = self._entry(key)
        if e is not None:
            return e.value
        else:
            return False

    def _entry(self, key):
        for e in self._entries:
            if e.key == key:
                return e
        return None

    def _entryiter(self):
        return (e for e in self._entries)

    def __len__(self):
        return len(self._entries)


map1 = ListMapping()
map1['New York'] = 'NY'
map1['Storrs'] = 'CT'
print('Mansfield' in map1)
print(map1)
