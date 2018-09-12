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

    def dfs(self, v):
        tree = {}
        tovisit = [(None, v)]
        while tovisit:
            a, b = tovisit.pop()
            if b not in tree:
                tree[b] = a
                for n in self.nbrs(b):
                    tovisit.append((b, n))
        return tree


V = {'A', 'B', 'C', 'D', 'E', 'F'}
E = {('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'A'),
     ('B', 'C'), ('C', 'B'), ('C', 'A'), ('C', 'D'),
     ('D', 'C'), ('D', 'A'), ('E', 'F'), ('F', 'E')}

graph = AdjacencySetGraph(V, E)
tree = graph.bfs('A')

print(tree)
for v in V:
    if v not in tree:
        print("The shortest distance between A and ", v, ":inf")
    else:
        count = {}
        for i in tree:
            count[tree[i]] = i

print("The shortest distance between A and ", v, ":", count)
