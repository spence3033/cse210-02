from Game.card import Card

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
            
            self.get_card_values()

            print(f"The card is: {self.card_value_1}")

            self.ask_for_hi_lo()
            self.update_total_score()

            print(f"Next card was: {self.card_value_2}")

            self.display_score()
            self.play_again()

    def get_card_values(self):
        '''Gives card 1 a value. Gives card 2 a value'''

        # If there is not a previous card value, game picks a random value
        # to begin the game.
        if self.card_value_1 == 0:
            self.card_value_1 = self.card.random_card()
            
        # If there is a previous card, use that value.
        else:
            self.card_value_1 = self.card_value_2

        # give card 2 a value
        self.card_value_2 = self.card.random_card()
            

    def ask_for_hi_lo(self):
        '''Display a card value to user. Ask the user if the next card value
           will be higher (h) or lower(l) and give user 100 points if the 
           guess was correct or subtract 75 if guess was incorrect.'''
        valid_input = False
        # Reset the user score to zero because it only keeps track of the 
        # most recent points won or lost by the user.

        #Loops until user gives a valid input
        while valid_input != True:
            choose_high_low = input("Higher or Lower? [h/l] ")

            # Check if user input is valid.
            if choose_high_low.lower() != "h" and choose_high_low.lower() != "l":
                print ("Error -Wrong input- Please try again.")
                valid_input = False
            else:
                valid_input = True

        # Check if user input is correct.
        if ((self.card_value_2 > self.card_value_1 and choose_high_low.lower() == "h") or
        (self.card_value_2 < self.card_value_1 and choose_high_low.lower() == "l")):
            self.score = 100
            
        # Points if user guess is incorrect. 
        else:
            self.score = -75
            

    def update_total_score(self):
        '''Update the total score.'''

        self.total_score += self.score

    def display_score(self):
        '''Display the total score.'''

        print(f"Your score is: {self.total_score}")
    
    def play_again(self):
        '''If total score is less than 0, end game loop. If not ask user
           to play again. '''

        if self.total_score <= 0:
            self.is_playing = False

        # Else ask user if he/she wants to continue playing the game. If user
        # enters anything but "y" game exits game loop. 
        else:
            continue_play = input("Play again? [y/n] ")
             
            self.is_playing = (continue_play.lower() == "y")

            print()

        



