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


# card = Card()
# card.random_card()
# print(card.value)
