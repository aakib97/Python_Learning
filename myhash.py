class MyHashtable:
    def __init__(self):
        self._numBuckets = 7
        # blist = [[]] * self._numBuckets
        # ^^^ That line does not work right. Why?
        blist = [[] for _ in range(self._numBuckets)]
        self._buckets = blist

    def __setitem__(self, key, value):
        hc = stringHash(str(key))
        bucketNum = hc % self._numBuckets
        bucket = self._buckets[bucketNum]
        entry = (key, value)
        bucket.append(entry)

    def __getitem__(self, key):
        hc = stringHash(str(key))
        bucketNum = hc % self._numBuckets
        bucket = self._buckets[bucketNum]
        values = [entry[1] for entry in bucket
                  if entry[0] == key]
        if values:
            return values[0]
        raise KeyError(key)


def stringHash(s):
    return sum([ord(c) for c in s[:4]]) + len(s)


def test():
    ht = MyHashtable()
    ht['Jeff'] = '555-1212'
    ht['Robert'] = '555-1234'
    ht['Alex'] = '123-4567'
    print('Buckets:')
    for n in range(len(ht._buckets)):
        print(n, ht._buckets[n])


if __name__ == '__main__':
    test()
