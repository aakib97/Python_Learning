import random


class ListNode:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def addfirst(self, item):
        self._head = ListNode(item, self._head)
        if self._tail is None:
            self._tail = self._head
        self._length += 1

    def addlast(self, item):
        if self._head is None:
            self.addfirst(item)
        else:
            self._tail.link = ListNode(item)
            self._tail = self._tail.link
            self._length += 1

    def removefirst(self):
        item = self._head.data
        self._head = self._head.link
        if self._head is None:
            self._tail = None
        self._length -= 1
        return item

    def removelast(self):
        if self._head is self._tail:
            return self.removefirst()
        else:
            currentnode = self._head
            while currentnode.link is not self._tail:
                currentnode = currentnode.link

            item = self._tail.data
            self._tail = currentnode
            self._tail.link = None
            self._length -= 1
            return item

    def __len__(self):
        return self._length

    # To-do: complete display function
    # the function should loop through all elements
    # and print each one
    # function ends with a print() for new line
    def display(self):
        node = self._head
        while node:
            print(node.data, end=' ')
            node = node.link

        print()  # new line

    def alldata(self):
        L = []
        cur = self._head
        while cur is not None:
            L.append(cur.data)
            cur = cur.link
        return L


class LinkedDeque:
    def __init__(self):
        self._L = LinkedList()

    def addfirst(self, item):
        self._L.addfirst(item)

    def removefirst(self):
        return self._L.removefirst()

    def addlast(self, item):
        self._L.addlast(item)

    def removelast(self):
        return self._L.removelast()

    def __len__(self):
        return len(self._L)

    def display(self):
        self._L.display()

    def alldata(self):
        return self._L.alldata()


def displaydeck(deck):
    for card in deck:
        print(card, end=' ')
    print()


def playgame(seed):
    # Shuffles deck and sets random seed.
    # Do not delete or alter
    deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4
    random.seed(seed)
    random.shuffle(deck)

    # To-do: split the deck in half using a list
    # assign 1 half to each player
    half = int(len(deck) / 2)
    top_deck = deck[0: half]
    bottom_deck = deck[half::]

    # To-do: after splitting the deck into 2 lists,
    # create a LinkedDeque instance for each player
    # in each LinkedDeque add that player's cards.
    player1 = LinkedDeque()
    player2 = LinkedDeque()
    for i in top_deck:
        player1.addlast(i)
    for i in bottom_deck:
        player2.addlast(i)

    # This is the public deck
    deckP = []
    counter = 0
    winner = 0
    cardP1 = 0
    cardP2 = 0
    end = False

    # To-do: Simulate the cycles of 1 game. See PDF for explanation.
    while not end:
        if counter == 0:
            rand = random.random()
            if rand > 0.5:
                cardP1 = player1.removelast()
            else:
                cardP1 = player1.removefirst()

            if cardP1 in deckP:
                deckP.append(cardP1)
                for i in deckP[deckP.index(cardP1):]:
                    player1.addlast(i)
                deckP = deckP[0:deckP.index(cardP1)]
            else:
                deckP.append(cardP1)

            if len(player1.alldata()) == 0:
                winner = ('B wins', player2.alldata())
                end = True
            counter += 1
        if counter == 1:
            rand = random.random()
            if rand > 0.5:
                cardP2 = player2.removelast()
            else:
                cardP2 = player2.removefirst()

            if cardP2 in deckP:
                deckP.append(cardP2)
                for i in deckP[deckP.index(cardP2):]:
                    player2.addlast(i)
                deckP = deckP[0:deckP.index(cardP2)]
            else:
                deckP.append(cardP2)

            if len(player2.alldata()) == 0:
                winner = ('A wins', player1.alldata())
                end = True
            counter = 0
    print(winner)
    return winner

    # To-do: Once a game has finished, return a tuple
    # which has either "A wins" or "B wins" as its first element
    # and the winning player's deck as a list as the second element