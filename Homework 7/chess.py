import random


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

    def randomdfs(self, v):

        ## Add your code here
        ## copy code from dfs and make changes
        ## only very small changes needed
        ## you need to use random.shuffle method
        tree = {}
        tovisit = [(None, v)]
        while tovisit:
            a, b = tovisit.pop()
            if b not in tree:
                tree[b] = a
                for n in self.nbrs(b):
                    tovisit.append((b, n))
        return tree


def knightsmove():
    b2 = 'b2'
    c2 = 'c2'
    d2 = 'd2'
    b3 = 'b3'
    d3 = 'd3'
    b4 = 'b4'
    c4 = 'c4'
    d4 = 'd4'
    e5 = 'e5'
    f5 = 'f5'
    g5 = 'g5'
    e6 = 'e6'
    g6 = 'g6'
    e7 = 'e7'
    f7 = 'f7'
    g7 = 'g7'

    V = [b2, c2, d2, b3, d3, b4, c4, d4, e5, f5, g5, e6, g6, e7, f7, g7]

    E = [(b2, c4), (b2, d3), (c2, b4), (c2, d4), (d2, b3), (d2, c4), (b3, d2), (b3, d4),
         (d3, b2), (d3, b4), (d3, e5), (b4, c2), (b4, d3), (c4, b2), (c4, d2), (c4, e5),
         (d4, b3), (d4, c2), (d4, e6), (d4, f5), (e5, c4), (e5, d3), (e5, f7), (e5, g6),
         (f5, d4), (f5, e7), (f5, g7), (g5, e6), (g5, f7), (e6, d4), (e6, g5), (e6, g7),
         (g6, e5), (g6, e7), (e7, f5), (e7, g6), (f7, e5), (f7, g5), (g7, e6), (g7, f5)]

    chessgraph = AdjacencySetGraph(V, E)

    ## We are repeating this at most 10000000 times to search for solutions
    ## We start from all the possible positions for the knight

    for i in range(1000000):
        for v in V:
            tree = chessgraph.randomdfs(v)
            if len(set(tree.values())) == len(V):
                inv_tree = {}
                for i in tree:
                    inv_tree[tree[i]] = i
                return inv_tree
    return None


inv_tree = knightsmove()
keys = set(inv_tree.keys())
values = set(inv_tree.values())
assert (len(keys) == 16)
assert (len(values) == 16)
assert(None in keys - values)
assert (len(keys ^ values) == 2)
print(inv_tree)
