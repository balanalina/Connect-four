from Game.game import board
from Game.game import gameException


class ui:
    def __init__(self,board):
        self._board = board
        
    def readMove(self):
        k = False
        while not k:
            try:
                column = int(input("Enter the column for your move: "))
                if type(column) != int or column<1 or column>7:
                    raise gameException("The column must be an integeger between 1 and 7! \n")
                k = True
            except gameException as e:
                print(e)
        return column
        
    def humanMove(self,column):
        self._board.move(column-1, "2")
        
    def computerMove(self,x):
        self._board.generateMove()
        
    def printBoard(self):
        print(self._board)
        print("\n");
        
    def start(self):
        gameOn = True
        playerTurn = True
        print("Match 4 to win! \n You are X, the computer is O!\n");
        self.printBoard()
        while gameOn:
            try:
                if playerTurn:
                    move = self.readMove()
                    self.humanMove(move)
                else:
                    self.computerMove(move-1)
                if self._board.tie() or self._board.win():
                    gameOn = False
                    if self._board.tie():
                        print("It is a tie! \n")
                    elif playerTurn:
                        print("You won! \n")
                    else:
                        print("You lost! \n")
                playerTurn = not playerTurn
                self.printBoard()
            except gameException as e:
                print(e)   
