import operator
import time


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


f = open('shakespeare.txt', 'r')
data = f.read()
f.close()

data = data.split()
start = time.time()

d = {}
for i in range(len(data)):
    key = data[i].lower()
    if key in d:
        d[key] += 1
    else:
        d[key] = 0

sorted_d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)

d_hash = HashMapping()
for i in range(len(data)):
    key = data[i].lower()
    if d.__contains__(key):
        d[key] += 1
    else:
        d[key] = 0

sorted_d_hash = sorted(d.items(), key=operator.itemgetter(1), reverse=True)

k = 0
count = 0
while count < 20:
    if sorted_d[k][0] not in {"'", ":", "!", ".", ",", ";", "?"}:
        print(count + 1, sorted_d[k])
        count += 1
    k += 1

end = time.time()

print(end - start)

k = 0
count = 0
while count < 20:
    if sorted_d_hash[k][0] not in {"'", ":", "!", ".", ",", ";", "?"}:
        print(count + 1, sorted_d[k])
        count += 1
    k += 1
