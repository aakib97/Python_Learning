class MyHashtable:

  def __init__(self):
    self._numBuckets = 7
    # blist = [[]] * self._numBuckets
    # ^^^ That line does not work right. Why? 
    blist = [[] for _ in range(self._numBuckets)]
    self._buckets = blist
    self._numEntries = 0

  def __setitem__(self, key, value):
    try:
      x = self[key]
    except:
      self._numEntries += 1
    hc = stringHash(str(key))
    bucketNum = hc % self._numBuckets
    bucket = self._buckets[bucketNum]
    entry = (key, value)
    bucket.append(entry)
    loadFactor = self._numEntries / len(self._buckets)
    if loadFactor > 0.7:
      self._resize()

  def _resize(self):
    print('<resizing>')
    oldSize = len(self._buckets)
    newSize = int(oldSize * 1.5)
    newBuckets = [[] for _ in range(newSize)]
    for bucket in self._buckets:
      for (key, value) in bucket:
        hc = stringHash(str(key))
        bucketNum = hc % newSize
        newBucket = newBuckets[bucketNum]
        newBucket.append((key, value))
    self._buckets = newBuckets
    self._numBuckets = newSize # I forgot this line when I wrote it in class!

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
  h = MyHashtable()
  print('Initial empty buckets:')
  for n in range(len(h._buckets)):
    print(n, h._buckets[n])
  h['a'] = 10
  h['b'] = 20
  h['c'] = 30
  h['d'] = 40
  h['e'] = 50 # this one causes a bucket resize
  h['f'] = 50
  print('After adding entries, buckets:')
  for n in range(len(h._buckets)):
    print(n, h._buckets[n])

  print('Retrieving each key:')
  for char in 'abcdef':
    print('h[', char, '] =', h[char])

if __name__ == '__main__':
  test()
