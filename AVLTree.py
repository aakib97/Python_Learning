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


class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self._length = 1

    def newnode(self, key, value):
        return BSTNode(key, value)

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
        # print("Put in BSTNode", self.key, self.value, key, value)
        if key == self.key:
            self.value = value
        elif key < self.key:
            if self.left:
                self.left = self.left.put(key, value)
            else:
                self.left = self.newnode(key, value)
        elif key > self.key:
            if self.right:
                self.right = self.right.put(key, value)
            else:
                self.right = self.newnode(key, value)
        self.updatelength()
        return self

    def updatelength(self):
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

    def rotateright(self):
        print("rotateright", self.key)
        newroot = self.left
        self.left = newroot.right
        newroot.right = self
        self.updatelength()
        newroot.updatelength()
        return newroot

    def rotateleft(self):
        print("rotateleft", self.key)
        newroot = self.right
        self.right = newroot.left
        newroot.left = self
        self.updatelength()
        newroot.updatelength()
        return newroot

    def maxnode(self):
        return self.right.maxnode() if self.right else self

    def _swapwith(self, other):
        ### Swap the key and value of a node.
        ### This operation has the potential to break the BST property.
        ### Use with caution!
        self.key, other.key = other.key, self.key
        self.value, other.value = other.value, self.value

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
        self.updatelength()
        return self

    def __iter__(self):
        if self.left: yield from self.left
        yield Entry(self.key, self.value)
        if self.right: yield from self.right

    def preorder(self):
        yield self.key
        if self.left: yield from self.left.preorder()
        if self.right: yield from self.right.preorder()

    def __len__(self):
        return self._length

    def __str__(self):
        return str(self.key) + " : " + str(self.value)


class BSTMapping(Mapping):
    Node = BSTNode

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

    def preorder(self):
        if self._root:
            yield from self._root.preorder()

    def __str__(self):
        return str(list(self.preorder()))

def height(node):
    return node.height if node else -1

def update(node):
    if node:
        node.updatelength()
        node.updateheight()

class AVLTreeNode(BSTNode):
    def __init__(self, key, value):
        BSTNode.__init__(self, key, value)
        self.updateheight()

    def newnode(self, key, value):
        return AVLTreeNode(key, value)

    def updateheight(self):
        self.height = 1 + max(height(self.left), height(self.right))

    def balance(self):
        return height(self.right) - height(self.left)

    def rebalance(self):
        # print('rebalance', self.key)
        bal = self.balance()
        if bal == -2:
            if self.left.balance() > 0:
                self.left = self.left.rotateleft()
            newroot = self.rotateright()
        elif bal == 2:
            if self.right.balance() < 0:
                self.right = self.right.rotateright()
            newroot = self.rotateleft()
        else:
            return self
        update(newroot.left)
        update(newroot.right)
        update(newroot)
        return newro

    def put(self, key, value):
        # print("Put in AVLTreeNode:", self.key, self.value, key, value)
        newroot = BSTNode.put(self, key, value)
        # print('newroot:', newroot.key)
        update(newroot)
        return newroot.rebalance()

    def remove(self, key):
        newroot = BSTNode.remove(self, key)
        update(newroot)
        return newroot.rebalance() if newroot else None


class AVLTreeMapping(BSTMapping):
    Node = AVLTreeNode


map1 = AVLTreeMapping()
map1['W'] = 1
print(map1)
map1['E'] = 2
print(map1)
map1['I'] = 3
print(map1)
map1['I'] = 4
print(map1)
map1['S'] = 5
print(map1)
map1['G'] = 6
print(map1)
map1['R'] = 7
print(map1)
map1['E'] = 8
print(map1)
map1['A'] = 9
print(map1)
map1['T'] = 10
print(map1)

print(map1.floor('Z'))
print("Number of nodes", len(map1))
print('Sum of values', sum(map1.values()))
