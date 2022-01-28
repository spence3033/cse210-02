import random

class Card:
    '''Card class will allow a game to implement choosing a random card from
       the values 1 to 13.'''

    def __init__(self):
        '''Constructs a new instance of a card that will have a value 
            attribute.'''
        self.value = 0

    def random_card(self):
        '''Generates a random number from 1 to 13.'''
        self.value = random.randint(1, 13)
        return self.value


# This was some code I used to test classes and how to access the attributes
# and how to use the methods of the class. It is completely irrelevant and 
# needs to be deleted before turning in our project, but if it is okay to 
# leave it here for now, it will help me rememember.
# card = Card()
# card.random_card()
# print(card.value)
