from ps9pr1 import Board

# write your class below.
class Player:
    def __init__(self, checker):
        """ constructs a new Player object
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
    
    def __repr__(self):
        """ returns a string representing a Player object.
        """
        return 'Player ' + self.checker
    
    def opponent_checker(self):
        """ returns a one-character string representing the 
            checker of the Player object’s opponent
        """
        if self.checker == "X":
            return 'O'
        return 'X'
    
    def next_move(self, b):
        """ accepts a Board object b as a parameter and returns 
            the column where the player wants to make the next move.
            Additionally, this method increments the number of moves 
            that the Player object has made
        """
        col = int(input("Enter a column: "))
        while b.can_add_to(col) == False:
            print('Try again!')
            col = int(input("Enter a column: "))
        self.num_moves += 1
        return col


        
    
    
