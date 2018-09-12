### Code for thought #8
### Amy's mom asked her to sort all her toy blocks, which are either red or green in color.
### All the red blocks need to be on the left of all the green blocks.
### For the blocks with the same color, larger volume ones need to be on the left.
### Help Amy get the job done by finishing the follow Block class, and fill in code for the
### method __lt__(self, other)

from random import randrange, seed

class Block:
    def __init__(self, color, length, width, depth):
        self.color = color
        self.length = length
        self.width = width
        self.depth = depth

    def volume(self):
        return self.length * self.width * self.depth

    def __lt__(self, other):
        if self.volume() > other.volume():
            return self.volume() > other.volume()
        return self.color > other.color

    def __str__(self):
        return str(self.color) + ' ' + str(self.length) + ' ' + str(self.width) \
               + ' ' + str(self.depth) + ' ' + str(self.volume())


