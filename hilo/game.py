from card import Card

class Game:
    '''The responsibility of the Game class is to control the sequence of the
       Hilo game play.'''

    def __init__(self):
        self.is_playing = True
        self.score = 0
        self.total_score = 300
        self.card = Card()
        self.card_value_1 = 0
        self.card_value_2 = 0
    
    def start_game(self):
        '''Starts the game by running the main game loop.'''

        # Continue to play the game until is_playing turns False.
        while self.is_playing:

            # If there is not a previous card value, game picks a random value
            # to begin the game.
            if self.card_value_1 == 0:
                self.card.random_card()
                self.card_value_1 = self.card.value
            
            # If there is a previous card, use that value.
            else:
                self.card_value_1 = self.card.value
            
            # Call method to choose a second random card to compare to the 
            # first card.
            self.card.random_card()
            self.card_value_2 = self.card.value

            # Call the method to get user input of higher or lower. If user
            # input is correct give 100 points to user, if incorrect user
            # gets -75.
            self.get_input()

            # Call method to update the user's total score.
            self.do_updates()
            self.do_outputs()

    def get_input(self):
        '''Display a card value to user. Ask the user if the next card value
           will be higher (h) or lower(l) and give user 100 points if the 
           guess was correct or subtract 75 if guess was incorrect.'''
        
        # Reset the user score to zero because it only keeps track of the 
        # most recent points won or lost by the user.
        self.score = 0
        print(f"The card is: {self.card_value_1}")
        choose_high_low = input("Higher or Lower? [h/l] ")

        # Check if user input is correct.
        if ((self.card_value_2 > self.card_value_1 and choose_high_low == "h") or
           (self.card_value_2 < self.card_value_1 and choose_high_low == "l")):
            self.score = 100
        
        # Points if user guess is incorrect. 
        else:
            self.score = -75
            

    def do_updates(self):
        '''Update the total score.'''
        self.total_score += self.score

    def do_outputs(self):
        '''Update the user of the value of the card, the score, and the
           total score. Ask if user wants to continue to play.'''
        
        # Print value of second card.
        print(f"The card was: {self.card_value_2}")

        # Print user's current total score.
        print(f"Your score is: {self.total_score}")

        # If user has a total score less than 0, end game loop.
        if self.total_score <= 0:
            self.is_playing = False

        # Else ask user if he/she wants to continue playing the game. If user
        # enters anything but "y" game exits game loop. 
        else:
            continue_play = input("Play again? [y/n] ")
            self.is_playing = (continue_play == "y")
            print()


game = Game()
game.start_game()
