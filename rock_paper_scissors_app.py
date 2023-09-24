import random

class RockPaperScissorsApp():
    """
       The RockPaperScissorsApp have six methods: getPlayerName, getPlayerSelection,
       generateRandomSelection and determineWinner.

       Attributes for the class:
       -player_name: expected to be a string
       -player_selection: expected to be a string
       -comp_selection = expected to be a string
    """

    def __init__(self):
        self.player_name = ""
        self.player_selection = ""
        self.computer_selection = ""

    #Method to get player's name
    def getPlayerName(self):
        self.player_name = input("Please enter your name: ")
        if self.player_name.lower() == 'quit':
            print("Thanks for playing!")
            return
        else:
            return self.player_name
    
    #Method to get user's selection
    def getPlayerSelection(self):
        while True:
            player_selection = input(f"{self.player_name.title()}, please enter 'Rock', 'Paper' or 'Scissors': ").lower()
            
            if player_selection == 'quit':
                print(f"Thanks for playing {self.player_name.title()}!")
                return None
            if player_selection in ('rock', 'paper', 'scissors'):
                self.player_selection = player_selection
                return self.player_selection.lower()
            else:
                print("Invalid answer. Please enter a valid answer")

    #Method to generate computer selection.
    def generateRandomSelection(self):
        choices = ["rock", "paper", "scissors"]
        self.computer_selection = random.choice(choices)
        return self.computer_selection

    #Method to determine the winner of the game.
    def determineWinner(self):
        self.generateRandomSelection()

        if self.computer_selection == self.player_selection:
            print(f"Game Tied! Computer chose: {self.computer_selection}")
        elif ((self.player_selection == "rock" and self.computer_selection =="paper") or
              (self.player_selection == "scissors" and self.computer_selection == "rock") or
              (self.player_selection == "paper" and self.computer_selection == "scissors")):
            print(f"You lose! Computer chose: {self.computer_selection}")
        else:
            print(f"You win! Computer chose: {self.computer_selection}")

#Function to run the RockPaperScissorsApp on instance.
def run():
    game = RockPaperScissorsApp()

    name = game.getPlayerName()
    if name is None:
        return
    
    while True:
        player_choice = game.getPlayerSelection()
        if player_choice is None:
            return
        
        game.determineWinner()

run()
