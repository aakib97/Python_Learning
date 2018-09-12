from fractions import Fraction
import itertools
import sys

ops = ['+', '-', '*', '/']
d = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 10, 'J': 11, 'Q': 12, 'K': 13}


class BNode:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None

    def addleft(self, leftnode):
        self.left = leftnode

    def addright(self, rightnode):
        self.right = rightnode

    def evaluate(self):
        if self.element in ops:
            ###get the card values
            if self.left.element in d:
                argument1 = d.get(self.left.element)
            else:
                argument1 = self.left.evaluate()
            if self.right.element in d:
                argument2 = d.get(self.right.element)
            else:
                argument2 = self.right.evaluate()
            ###Operations
            if self.element == '+':
                return argument1 + argument2
            elif self.element == '-':
                return argument1 - argument2
            elif self.element == '*':
                return argument1 * argument2
            elif self.element == '/':
                if argument2 == 0:
                    return 0
                else:
                    return Fraction(argument1, argument2)
        else:
            return self.element

    def display(self):
        if self.element in ops:
            ###get the card values
            if self.right.element in d:
                argument2 = d.get(self.right.element)
            else:
                argument2 = self.right.display()
            if self.left.element in d:
                argument1 = d.get(self.left.element)
            else:
                argument1 = self.left.display()
            ###Operations
            if self.element == '+':
                return '(' + str(argument1) + '+' + str(argument2) + ')'
            elif self.element == '-':
                return '(' + str(argument1) + '-' + str(argument2) + ')'
            elif self.element == '*':
                return '(' + str(argument1) + '*' + str(argument2) + ')'
            elif self.element == '/':
                if argument2 == 0:
                    return '(' + str(0) + ')'
                else:
                    return '(' + str(argument1) + '/' + str(argument2) + ')'
        else:
            print(str(self.element))


def evaluatefive(ops, cards):
    s = set()
    # Tree #1        
    node1 = BNode(ops[0])

    node2 = BNode(ops[1])
    node3 = BNode(ops[2])
    node1.addleft(node2)
    node1.addright(node3)

    node4 = BNode(cards[0])
    node5 = BNode(cards[1])

    node6 = BNode(cards[2])
    node7 = BNode(cards[3])

    node2.addleft(node4)
    node2.addright(node5)

    node3.addleft(node6)
    node3.addright(node7)

    if node1.evaluate() == 24:
        s.add(node1.display())

    # Tree #2
    node1 = BNode(ops[0])

    node2 = BNode(ops[1])
    node3 = BNode(cards[3])
    node1.addleft(node2)
    node1.addright(node3)

    node4 = BNode(ops[2])
    node5 = BNode(cards[2])

    node6 = BNode(cards[0])
    node7 = BNode(cards[1])

    node2.addleft(node4)
    node2.addright(node5)

    node4.addleft(node6)
    node4.addright(node7)

    if node1.evaluate() == 24:
        s.add(node1.display())

    # Tree #3
    node1 = BNode(ops[0])

    node2 = BNode(cards[0])
    node3 = BNode(ops[1])
    node1.addleft(node2)
    node1.addright(node3)

    node4 = BNode(ops[2])
    node5 = BNode(cards[3])

    node6 = BNode(cards[1])
    node7 = BNode(cards[2])

    node3.addleft(node4)
    node3.addright(node5)

    node4.addleft(node6)
    node4.addright(node7)

    if node1.evaluate() == 24:
        s.add(node1.display())

    #Tree #4
    node1 = BNode(ops[0])

    node2 = BNode(cards[0])
    node3 = BNode(ops[1])
    node1.addleft(node2)
    node1.addright(node3)

    node4 = BNode(ops[2])
    node5 = BNode(cards[1])

    node6 = BNode(cards[2])
    node7 = BNode(cards[3])

    node3.addleft(node4)
    node3.addright(node5)

    node4.addleft(node6)
    node4.addright(node7)

    if node1.evaluate() == 24:
        s.add(node1.display())

    # Tree #5
    node1 = BNode(ops[0])

    node2 = BNode(cards[0])
    node3 = BNode(ops[1])
    node1.addleft(node2)
    node1.addright(node3)

    node4 = BNode(cards[1])
    node5 = BNode(ops[2])

    node6 = BNode(cards[2])
    node7 = BNode(cards[3])

    node3.addleft(node4)
    node3.addright(node5)

    node5.addleft(node6)
    node5.addright(node7)

    if node1.evaluate() == 24:
        s.add(node1.display())

    return s

s = list(input())
if len(s) != 4:
    sys.exit()
for i in range(len(s)):
    if s[i] not in d.keys():
        sys.exit()
results = set()
s1 = [0, 1, 2, 3]
for L in list(itertools.permutations([0, 1, 2, 3], 4)):
    for i in range(4):
        s1[i] = s[L[i]]

    ops1 = [ops[0], ops[0], ops[0]]
    for i in range(len(ops)):
        for j in range(len(ops)):
            for k in range(len(ops)):
                ops1[0] = ops[i]
                ops1[1] = ops[j]
                ops1[2] = ops[k]
                results = results | evaluatefive(ops1, s1)
for result in results:
    print(result)
print(str(len(results)) + " solutions.")

