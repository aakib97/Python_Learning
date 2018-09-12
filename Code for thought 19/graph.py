### Code for thought #19
### Understanding BFS and DFS
### In this assignment, we use two simple graphs to show how BFS and DFS behaves
### These examples will give us some intuition on when to use BFS and when to use
### DFS.


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

    def bfs_print(self, v):
        tree = {}
        tree = self.bfs(v)
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

    def dfs_print(self, v):
        tree = {}
        tree = self.dfs(v)
        return tree


### Use fig 1 in the pdf file to construct the first graph
### You need to specify the edges

V = {'O', 'A', 'B', 'C', 'D', 'E', 'F'}
### Add your code to specify the edges
E = {('O', 'A'), ('A', 'O'), ('O', 'B'), ('B', 'O'), ('O', 'C'), ('C', 'O'), ('O', 'D'), ('D', 'O'),
     ('O', 'E'), ('E', 'O'), ('O', 'F'), ('F', 'O'), ('A', 'B'), ('B', 'A'), ('B', 'C'), ('C', 'B'),
     ('C', 'D'), ('D', 'C'), ('D', 'E'), ('E', 'D'), ('E', 'F'), ('F', 'E'), ('F', 'A'), ('A', 'F'), }

graph = AdjacencySetGraph(V, E)
print("bfs traversal:")
tree_bfs = graph.bfs_print('O')
print("bfs tree:")
print(tree_bfs)
assert(set(tree_bfs.values()) - {None} == {'O'})
print("Set of parents in the bfs tree:")
print(set(tree_bfs.values()) - {None})

print("++++++++++++++++++++++++++++++++++++++++++++++++")
print("dfs traversal:")
tree_dfs = graph.dfs_print('O')
print("dfs tree:")
print(tree_dfs)
print("Set of parents in the dfs tree:")
print(set(tree_dfs.values()) - {None})
assert (len(set(tree_dfs.values())) == len(V))

### Try to understand why the above assert satements are true
### Draw the bfs tree and the dfs tree and what do you notice?
### If you run the code multiple times, you might notice that the
### dfs tree is not unique. Why is that?


print("************************************************")
### Use fig 2 in the pdf file to construct the second graph
### You need to specify the edges

V = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
### Add your code to specify the edges
E = {(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6), (3, 7), (3, 8), (4, 9), (4, 10),
     (5, 11), (5, 12), (6, 13), (6, 14)}

graph = AdjacencySetGraph(V, E)
print("bfs traversal:")
tree_bfs = graph.bfs_print(0)
print("bfs tree:")
print(tree_bfs)
print("+++++++++++++++++++++++++++++++++++++++++++++++++")
print("dfs traversal:")
tree_dfs = graph.dfs_print(0)
print("dfs tree:")
print(tree_dfs)
assert (tree_bfs == tree_dfs)

### Try to understand why the above assert statement is true
### Draw the bfs tree and dfs tree and what do you notice?
