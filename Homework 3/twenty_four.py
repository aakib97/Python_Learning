from fractions import Fraction
import itertools
import operator

ops = ['+', '-', '*', '/']
d = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 10, 'J': 11, 'Q': 12, 'K': 13}


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


# evaluate(s) takes in a list s containg an expression in postfix notation as an argument
# and uses the stack to evaluate the expression.
def evaluate(s):
    stack = ListStack()
    convert = []
    for x in s:
        temp = d.get(x)
        if temp:
            convert.append(temp)
        else:
            convert.append(x)

    s = convert
    for i in s:
        stack.push(i)

    def operation(item):
        argument2 = stack.pop()
        argument1 = stack.pop()
        if item == '+':
            stack.push(argument1 + argument2)
        elif item == '-':
            stack.push(argument1 - argument2)
        elif item == '*':
            stack.push(argument1 * argument2)
        elif item == '/':
            if argument2 == 0:
                stack.push(0)
            else:
                stack.push(Fraction(argument1, argument2))

    for element in s:
        if element == '+':
            operation('+')
        elif element == '-':
            operation('-')
        elif element == '*':
            operation('*')
        elif element == '/':
            operation('/')
        else:
            stack.push(element)
    return stack.pop()



# s: list containing the 4 randomly chosen cards
# Generates and evaluates all valid postfix notations for the 4 cards.
# Adds expressions to results if they evaluate to 24.
def evaluate_all_ops(s):
    results = set()
    notation_1 = []
    notation_2 = []
    notation_3 = []
    notation_4 = []
    notation_5 = []

    for x in ops:
        for y in ops:
            for z in ops:
                notation_1.append(s[0]), notation_1.append(s[1]), notation_1.append(z), notation_1.append(s[2]), notation_1.append(s[3]), notation_1.append(y), notation_1.append(x)
                not1_test = evaluate(notation_1)
                if not1_test == 24:
                    results.add(str(list(notation_1)))
                else:
                    notation_1 = []
                notation_2.append(s[0]), notation_2.append(s[1]), notation_2.append(s[2]), notation_2.append(s[3]), notation_2.append(z),  notation_2.append(y), notation_2.append(x)
                not2_test = evaluate(notation_2)
                if not2_test == 24:
                    results.add(str(list(notation_2)))
                else:
                    notation_2 = []
                notation_3.append(s[0]), notation_3.append(s[1]), notation_3.append(s[2]), notation_3.append(z), notation_3.append(s[3]), notation_3.append(y), notation_3.append(x)
                not3_test = evaluate(notation_3)
                if not3_test == 24:
                    results.add(str(list(notation_3)))
                else:
                    notation_3 = []
                notation_4.append(s[0]), notation_4.append(s[1]), notation_4.append(z), notation_4.append(s[2]), notation_4.append(y), notation_4.append(s[3]), notation_4.append(x)
                not4_test = evaluate(notation_4)
                if not4_test == 24:
                    results.add(str(list(notation_4)))
                else:
                    notation_4 = []
                notation_5.append(s[0]), notation_5.append(s[1]), notation_5.append(s[2]), notation_5.append(z), notation_5.append(y), notation_5.append(s[3]), notation_5.append(x)
                not5_test = evaluate(notation_5)
                if not5_test == 24:
                    results.add(str(list(notation_5)))
                else:
                    notation_5 = []
    return results
