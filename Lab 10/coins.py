## This problem is from the book "Perplexing Puzzles and Trantalizing Teasers" by Martin Gardner
from itertools import permutations


class Queue:
    def __init__(self):
        self._head = 0
        self._L = []

    def enqueue(self, item):
        self._L.append(item)

    def dequeue(self):
        item = self._L[self._head]
        self._head += 1
        return item

    def __len__(self):
        return len(self._L) - self._head

    def isempty(self):
        return len(self) == 0


class AdjacencySetGraph:
    def __init__(self, V, E):
        self._V = set()
        self._nbrs = {}
        for v in V: self.addvertex(v)
        for u, v in E: self.addedge(u, v)

    def vertices(self):
        return iter(self._V)

    def edges(self):
        for u in self._V:
            for v in self.nbrs(u):
                yield (u, v)

    def addvertex(self, v):
        self._V.add(v)
        self._nbrs[v] = set()

    def addedge(self, u, v):
        self._nbrs[u].add(v)

    def nbrs(self, v):
        return iter(self._nbrs[v])

    def bfs(self, v):
        tree = {}

        tovisit = Queue()
        tovisit.enqueue((None, v))
        while tovisit:
            a, b = tovisit.dequeue()
            if b not in tree:
                tree[b] = a
                for n in self.nbrs(b):
                    tovisit.enqueue((b, n))
        return tree

    def showresult(self, u, v):
        ## Add your code here
        ## We first do BFS starting from u
        ## Then we check whether v is in the BFS tree
        ## If so, we print out the solution
        ## Also we put the solutions in a list return it
        result = []
        tree = self.bfs(u)
        if v in tree:
            for i in range(9):
                print(v)
                result.append(v)
                v = tree.get(v)
            result.reverse()
        return result


def isneighbor(v1, v2):
    ## Add your code here
    ## Note the function should return Boolean values
    v1_list = list(v1)
    v2_list = list(v2)
    emptyspace1 = v1_list.index(0)
    emptyspace2 = v2_list.index(0)
    if emptyspace2 == emptyspace1 - 1 or emptyspace2 == emptyspace1 + 1:
        v2_list[emptyspace2] = v2_list[emptyspace1]
        v2_list[emptyspace1] = 0
        if v1_list == v2_list:
            return True
        else:
            return False
    elif emptyspace2 == emptyspace1 - 2 or emptyspace2 == emptyspace1 + 2:
        v2_list[emptyspace2] = v2_list[emptyspace1]
        v2_list[emptyspace1] = 0
        if v1_list == v2_list:
            return True
        else:
            return False
    else:
        return False


isneighbor((1, 1, 0, 10, 10), (1, 0, 1, 10, 10))


def createedges(V):
    E = set()
    for u in V:
        for v in V:
            if isneighbor(u, v):
                E.add((u, v))
    return E


def dime_and_penny():
    items = [1, 1, 0, 10, 10]
    V = set()
    for p in permutations(items):
        V.add(p)
    E = createedges(V)

    coinsgraph = AdjacencySetGraph(V, E)
    return coinsgraph.showresult((1, 1, 0, 10, 10), (10, 10, 0, 1, 1))


result = dime_and_penny()
print("***********************")
for v in result:
    print(v)
