class ListStack:
    def __init__(self):
        self._L = []

    def push(self, item):
        self._L.append(item)

    def pop(self):
        return self._L.pop()

    def peek(self):
        return self._L[-1]

    def __len__(self):
        return len(self._L)

    def isempty(self):
        return len(self) == 0


def match(exp):
    d = {'(': ')', '{': '}', '[': ']'}
    L = list(exp)
    stack = ListStack()
    for c in L:
        if c in d:
            stack.push(c)
        if c in d.values():
            if stack.isempty():
                return False
            test = stack.pop()
            if d[test] != c:
                return False
    if stack.isempty():
        return True

    return stack.isempty()
