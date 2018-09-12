class ListNode:
    def __init__(self, data, prev = None, link = None):
        self.data = data
        self.prev = prev
        self.link = link
        if prev is not None:
            self.prev.link = self
        if link is not None:
            self.link.prev = self

class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail
    
    def _addbetween(self, item, before, after):
        node = ListNode(item, before, after)
        if after is self._head:
            self._head = node
        if before is self._tail:
            self._tail = node
        self._length += 1

    def addfirst(self, item):
        self._addbetween(item, None, self._head)
        
    def addlast(self, item):
        self._addbetween(item, self._tail, None)

    def _remove(self, node):
        before, after = node.prev, node.link
        if node is self._head:
            self._head = after
        else:
            before.link = after
        if node is self._tail:
            self._tail = before
        else:
            after.prev = before
        self._length -= 1
        return node.data

    def removefirst(self):
        return self._remove(self._head)

    def removelast(self):
        return self._remove(self._tail)
    
    def __len__(self):
        return self._length


## To-do : Complete the tolinkednumber and __str__ funtions.
class DoublyLinkedNumber(DoublyLinkedList):
    
    ## Iterate over each charater in the string
    ## and add it to the last of the doubly linked list
    def tolinkednumber(self, string):
        for i in string:
            self.addlast(i)
        cur = self.head
        while cur:
            if cur.data == '0':
                self.removefirst()
                cur = cur.link
            else:
                break


    ## Traverse the list and convert data in each node to string
    def __str__(self):
        cur = self._head
        s = ''
        while cur:
            s += str(cur.data)
            s += ''
            cur = cur.link
        s.rstrip()
        return s

## To-Do : Addition of numbers present in the 2 DoublyLinkedLists.
## Start from the tail and traverse backwards.
## Perform addition on data of nodes and account for carry generated
## Store the sum in a new doubly linked list
def sumlinkednumbers(dll1, dll2):
    dllsum = DoublyLinkedNumber()
    cur1 = dll1.tail
    cur2 = dll2.tail
    carry = 0
    while dll1.__len__() > dll2.__len__():
        dll2.addfirst('0')
    while dll2.__len__() > dll1.__len__():
        dll1.addfirst('0')
    while cur1:
        sum = int(cur1.data) + int(cur2.data) + carry
        if sum > 10:
            carry = int((sum - (sum - 10))/10)
            dllsum.addfirst(str(sum-10))
            cur1 = cur1.prev
            cur2 = cur2.prev
        else:
            carry = 0
            dllsum.addfirst(str(sum))
            cur1 = cur1.prev
            cur2 = cur2.prev
    cur_sum = dllsum.head
    while cur_sum:
        if cur_sum.data == '0':
            dllsum.removefirst()
            cur_sum = cur_sum.link
        else:
            break
    return dllsum.__str__()

s1 = '156697122'
dll1 = DoublyLinkedNumber()
dll1.tolinkednumber(s1)
s2 = '100223'
dll2 = DoublyLinkedNumber()
dll2.tolinkednumber(s2)

print(sumlinkednumbers(dll1,dll2))