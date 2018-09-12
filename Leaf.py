class Tree:
    def __init__(self, L):
        iterator = iter(L)
        self.data = next(iterator)
        self.children = [Tree(c) for c in iterator]

    def printpreorder(self):
        print(self.data)
        for child in self.children:
            child.printpreorder()

    def printpostorder(self):
        for child in self.children:
            child.printpostorder()
        print(self.data)

    def leafnum(self):
        count = 1
        for child in self.children:
            if not child.children:
                count += child.leafnum()
        return count


T = [0, [1, [2], [3]], [4, [5], [6], [7]], [8]]
treeBook = Tree(T)
print("Number of leaf nodes:", treeBook.leafnum())
print("Postorder traversal:")
treeBook.printpostorder()
print("Preorder traversal:")
treeBook.printpreorder()
