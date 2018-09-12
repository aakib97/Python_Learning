## Code for thought #18
## In this assignment, we are going to implement a few methods for BSTMapping
## 1. Initializer: make sure we can use a list to do initilization
## 2. height: height of binary search tree
## 3. preorder: pre-order traversal of the binary search tree


class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) + ' : ' + str(self.value)


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
        # print(self, "contains", key)
        try:
            return self.get(key) is not None
        except KeyError:
            return False

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __str__(self):
        return "{%s}" % (", ".join([str(e) for e in self._entryiter()]))


class BSTMapping(Mapping):
    def __init__(self, L=None):
        if L is None:
            self._root = None
        else:
            for i in L:
                if L.index(i) == 0:
                    self._root = BSTNode(i[0], i[1])
                else:
                    self.__setitem__(i[0], i[1])

    def get(self, key):
        if self._root:
            return self._root.get(key).value
        raise KeyError

    def put(self, key, value):
        if self._root:
            self._root.put(key, value)
        else:
            self._root = BSTNode(key, value)

    def __len__(self):
        return len(self._root) if self._root else 0

    def height(self):
        if self._root is None:
            return 0
        else:
            return BSTNode.height(self._root)

    def _entryiter(self):
        if self._root:
            yield from self._root

    def floor(self, key):
        if self._root:
            floornode = self._root.floor(key)
            if floornode is not None:
                return floornode.key, floornode.value
        return None, None

    def remove(self, key):
        if self._root:
            self._root = self._root.remove(key)
        else:
            raise KeyError

    def __delitem__(self, key):
        self.remove(key)

    def preorder(self):
        if self._root is None:
            return 0
        else:
            print(BSTNode.preorder(self._root))


class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self._length = 1

    def __len__(self):
        return self._length

    def height(self):
        if self.left is not None and self.right is not None:
            if len(self.left) >= len(self.right):
                return len(self.left)
            elif len(self.right) >= len(self.left):
                return len(self.right)
        elif self.left is not None and self.right is None:
            return len(self.left)
        elif self.right is not None and self.left is None:
            return len(self.right)
        else:
            return 0

    def get(self, key):
        if key == self.key:
            return self
        elif key < self.key and self.left:
            return self.left.get(key)
        elif key > self.key and self.right:
            return self.right.get(key)
        else:
            raise KeyError

    def put(self, key, value):
        if key == self.key:
            self.value = value
        elif key < self.key:
            if self.left:
                self.left.put(key, value)
            else:
                self.left = BSTNode(key, value)
        elif key > self.key:
            if self.right:
                self.right.put(key, value)
            else:
                self.right = BSTNode(key, value)
        self._updatelength()

    def _updatelength(self):
        len_left = len(self.left) if self.left else 0
        len_right = len(self.right) if self.right else 0
        self._length = 1 + len_left + len_right

    def floor(self, key):
        if key == self.key:
            return self
        elif key < self.key:
            return self.left.floor(key) if self.left else None
        elif key > self.key:
            return (self.right.floor(key) or self) if self.right else self

    ## This is inorder traversal
    def __iter__(self):
        if self.left:
            yield from self.left
        yield self
        if self.right:
            yield from self.right

    def _swapwith(self, other):
        self.key, other.key = other.key, self.key
        self.value, other.value = other.value, self.value

    def maxnode(self):
        return self.right.maxnode() if self.right else self

    def remove(self, key):
        if key == self.key:
            if self.left is None: return self.right
            if self.right is None: return self.left
            self._swapwith(self.left.maxnode())
            self.left = self.left.remove(key)
        elif key < self.key and self.left:
            self.left = self.left.remove(key)
        elif key > self.key and self.right:
            self.right = self.right.remove(key)
        else:
            raise KeyError
        self._updatelength()
        return self

    def __str__(self):
        return str(self.key) + ':' + str(self.value)

    def preorder(self):
        if self.left is not None:
            print(self)
            self.left.preorder()
        elif self.right is not None:
            print(self)
            self.right.preorder()


map1 = BSTMapping()

print("height:", map1.height())

map1[1] = 'one'
print("height:", map1.height())

map1[2] = 'two'
print("height:", map1.height())

map1[3] = 'three'
print("height:", map1.height())

map1[4] = 'four'
print("height:", map1.height())

map1[5] = 'five'
print("height:", map1.height())
print("in-order:")
print(map1)
print("pre-order:")
map1.preorder()

print("\n****************************************************************")
L = [(1, "ONE"), (2, "TWO"), (3, "THREE"), (4, "FOUR"), (5, "FIVE")]
print(L)
map2 = BSTMapping(L)
print("in-order:")
print(map2)
print("height:", map2.height())
print("pre-order:")
map2.preorder()

print("\n****************************************************************")
L = [(3, "THREE"), (2, "TWO"), (4, "FOUR"), (1, "ONE"), (5, "FIVE")]
print(L)
map2 = BSTMapping(L)
print("in-order:")
print(map2)
print("height:", map2.height())
print("pre-order:")
map2.preorder()

print("\n****************************************************************")
L = [(5, "FIVE"), (4, "FOUR"), (3, "THREE"), (2, "TWO"), (1, "ONE")]
print(L)
map2 = BSTMapping(L)
print("in-order:")
print(map2)
print("height:", map2.height())
print("pre-order:")
map2.preorder()

print("\n****************************************************************")
L = [(3, "THREE"), (2, "TWO"), (1, "ONE"), (4, "FOUR"), (5, "FIVE")]
print(L)
print("in-order:")
map2 = BSTMapping(L)
print(map2)
print("height:", map2.height())
print("pre-order:")
map2.preorder()
