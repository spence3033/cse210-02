from card import Card

class Game:
    '''The responsibility of the Game is to control the sequence of play.'''

    def __init__(self):
        self.is_playing = True
        self.score = 0
        self.total_score = 300
        self.card = Card()
        self.card_value_1 = 0
        self.card_value_2 = 0
    
    def start_game(self):
        '''Starts the game by running the main game loop.'''

        while self.is_playing:
            if self.card_value_1 == 0:
                self.card.random_card()
                self.card_value_1 = self.card.value
            else:
                self.card_value_1 = self.card.value

            self.card.random_card()
            self.card_value_2 = self.card.value

            self.get_input()
            self.do_updates()
            self.do_outputs()
            # self.continue_play()

    def get_input(self):
        '''Ask the user if the number is higher (h) or lower(l).'''
        self.score = 0
        print(f"The card is: {self.card_value_1}")
        choose_high_low = input("Higher or Lower? [h/l] ")
        if ((self.card_value_2 > self.card_value_1 and choose_high_low == "h") or
           (self.card_value_2 < self.card_value_1 and choose_high_low == "l")):
            self.score = 100
        else:
            self.score = -75
            

    def do_updates(self):
        '''Update the total score.'''
        self.total_score += self.score

    def do_outputs(self):
        '''Update the user of the value of the card, the score, and the
           total score. Ask if user wants to continue to play.'''
        print(f"The card was: {self.card_value_2}")
        print(f"Your score is: {self.total_score}")
        if self.total_score <= 0:
            self.is_playing = False
        else:
            continue_play = input("Play again? [y/n] ")
            self.is_playing = (continue_play == "y")
            print()

        





game = Game()
game.start_game()
