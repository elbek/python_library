import random

__author__ = 'ekamoliddinov'
class Book:
    def __init__(self, title):
        self.title = title
        self.copies = random.randint(2, 4) #has to be random
        self.taken = 0

    def __hash__(self):
        return hash(self.title)

    def __eq__(self, other):
        return self.title == other.title
