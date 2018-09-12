## Code for thought 15

## In this excercise, we study the implementation of HashMapping.
## We will finish the class HashMapping by implementing the get method.

class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) + ': ' + str(self.value)


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
        try:
            return (self.get(key) is not None)
        except KeyError:
            return False

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
            raise KeyError

    def _entry(self, key):
        for e in self._entries:
            if e.key == key:
                return e
        return None

    def _entryiter(self):
        return (e for e in self._entries)

    def __len__(self):
        return len(self._entries)


class HashMapping(Mapping):
    def __init__(self, size=100):
        self._size = size
        self._buckets = [ListMapping() for i in range(self._size)]
        self._length = 0

    def _entryiter(self):
        return (e for b in self._buckets for e in b._entryiter())

    def get(self, key):
        e = self._bucket(key)
        if e is not None:
            return e[key]
        else:
            raise KeyError

    def put(self, key, value):
        b = self._bucket(key)
        if key not in b:
            self._length += 1
        b[key] = value
        if self._length > self._size:
            self._double()

    def __len__(self):
        return self._length

    def _bucket(self, key):
        return self._buckets[hash(key) % self._size]

    def _double(self):
        # Save the old buckets
        oldbuckets = self._buckets
        # Reinitialize with more buckets.
        self.__init__(self._size * 2)
        for bucket in oldbuckets:
            for key, value in bucket.items():
                self[key] = value


map1 = HashMapping()
map1[4] = 'four'
map1[5] = 'five'
map1[8] = 'eight'
map1[108] = 'one hundred and eight'
print(map1[108])

print(9999 in map1)
print('four' in map1.values())
print(map1)

for i in range(10):
    map1[i] = i

print(99 in map1)
print('four' in map1.values())
print(map1)
print('length:', len(map1))

## Note if you run the code multiple times, the following results might change.
## This tells us that we should not assume that keys and values in a dictionary
## have deterministic orders

print(hash(('Wei Wei', 123456789)))
print(hash('New York'))
print(hash('Connecticut'))

map1[('Wei Wei', 123456789)] = 'A Great Guy'
map1['New York'] = 'NY'
map1['Connecticut'] = 'CT'
map1['six'] = 6
map1['seven'] = 7

print('length:', len(map1))
print("The map:")
print(map1)
print("keys:")
for k in map1:
    print(k)

print("values:")
for v in map1.values():
    print(v)
