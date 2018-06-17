import random
class RockPaperScissors:
    """
    Implementation of the game Rock, Paper, Scissors
    """
    def __init__(self): #i will need these variables
        self.computerchoice = None
        self.humanchoice = None
        self.paper = {'rock': True, 'scissors' : False }
        self.rock = {'paper': True, 'scissors' : False}
        self.scissors = {'paper' : True, 'rock': False}
        self.choice = {'paper' : self.paper, 'rock' : self.rock, 'scissors': self.scissors}
        self.wincounter = 0
        self.losscounter = 0
        self.playagain = None
        pass

    def computer_choice(self):
        """
        The computer chooses a value
        """
        self.computerchoice = random.choice(['rock', 'paper', 'scissors'])
        return self.computerchoice

    def human_choice(self):
        """
        The human player chooses a value
        """
        while answer not in choices:
            self.humanchoice = input("input 'rock' paper' or 'scissors")

        return self.humanchoice


    def evaluate_game(self):
        """
        Evaluate the values of the two players
        """
        if self.computerchoice == self.humanchoice :
            print('tied game')

        else:
            if self.choice[self.humanchoice][self.computerchoice]:
                print('win')
                self.wincounter +=1
                return self.wincounter
            else:
                print('loss')
                self.losscounterounter += 1
                return self.losscounter


 ####  def print_result(self):
 ##      """
 ##      Visualise game result
 ##      """
 ##
 ##      pass

 #   def count_points(self):
 #       """
 #       Count the points of all rounds
 #       """
 #       pass
#
    def new_game_question(self):
        """
        Ask human player for new game
        """
        print("you have won", self.wincounter,  "times and lost", self.losscounter, "times" )
        self.playagain = input("would you like to play again [y/n]")

        if self.playagain:
            return RockPaperScissors()
        else:
            pass


if __name__ == "__main__":
    RockPaperScissors()