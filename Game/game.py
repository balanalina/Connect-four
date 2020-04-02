from texttable import Texttable
from random import choice
import unittest

class gameException(Exception):
    def __init__(self,msg):
        self._msg = msg
        
    def message(self):
        return self._msg
    
class board:
    def __init__(self):
        self._data = [0] * 42
    """
    0 - empty square
    -1 - computer
    1 - player
    """    
    def move(self,c,player):
        if c < 0 or c > 6:
            raise gameException("This column is outside the board. Chose a column between 1 and 7! \n")
        line = 5
        k = False
        while line >= 0 and not k:
            if self._data[line*7 + c] != 0:
                line -= 1
            else:
                k = True
        if not k:
            print(c)
            raise gameException("There is no empty line on this column! \n")
        dict = { "1" : -1 , "2" : 1}
        self._data[line * 7 + c] = dict[player]
        
    def generateMove(self):
        line = 5
        k = False
        while line > 0 and not k:
            for i in range(7):
                if self._data[7*line+i] != 0:
                    if self.checkLineC(line, i):
                        if self._data[7*line + i+3] == 0:
                            self.move(i+3, "1") 
                            k = True
                    elif self.checkColumnC(line, i):
                        if self._data[7*(line-3)+i] == 0:
                            self.move(i,"1")
                            k = True
                    elif self.checkDPC(line, i):
                        if self._data[7*(line -2)+i+2] != 0 and self._data[7*(line-3)+i+3] == 0:
                            self.move(i+3,"1")
                            k = True
                    elif self.checkDSC(line, i):
                        if  self._data[7*(line -2)+i-2] !=0 and self._data[7*(line-3)+i-3] == 0:
                            self.move(i-3,"1")
                            k = True
            line -=1
        if not k:
            list = self.getEmptySquares()
            #print(list)
            self.move(choice(list)//7,"1")
                    
    #checks for best move generation

    def checkLineC(self,line,column):
        if column >3 :
            return False
        return self._data[7*line+column] == self._data[7*line+column+1] and self._data[7*line+column+1] == self._data[7*line+column+2] 
        
    def checkColumnC(self,line,column):
        if line < 3 :
            return False
        return self._data[7*line+column] == self._data[7*(line -1)+column] and self._data[7*(line -1)+column] == self._data[7*(line -2)+column] 

    def checkDPC(self,line,column):
        if line < 3 or column > 3:
            return False
        return self._data[7*line+column] == self._data[7*(line -1)+column+1] and self._data[7*(line -1)+column+1] == self._data[7*(line -2)+column+2]  

    def checkDSC(self,line,column):
        if column < 3 or line <3:
            return False
        return self._data[7*line + column] == self._data[7*(line -1)+column-1] and self._data[7*(line -1)+column-1] == self._data[7*(line -2)+column-2] 
    
        
    """
    ' ' - empty square
    'O' - computer
    'X' - player
    """       
    def __str__(self):
        t = Texttable()   
        dict = {0:" ",1:"X",-1:"O"}
        for i in range(6):
            list = self._data[7*i:7*i+7]
            for j in range(7):
                list[j] = dict[list[j]]
            t.add_row(list)
        return t.draw()
    """
    We put into the empty list the indexes of the empty squares.
    """
    def getEmptySquares(self):
        emptyList = []
        for i in range(42):
            if self._data[i] == 0:
                emptyList.append(i)
        return emptyList
                
    def tie(self):
        return len(self.getEmptySquares()) == 0 and not self.win()
    
    def getBoard(self):
        return self._data


    def win(self):
        line = 5
        while line>0:
            for i in range(7):
                if self._data[line*7 + i] != 0:
                    if self.checkLine(line, i) or self.checkColumn(line, i) or self.checkDP(line, i) or self.checkDS(line, i):
                        return True
            line -= 1
        return False

    #checks lines for a win
    def checkLine(self,line,column):
        if column >3:
            return False
        return self._data[7*line+column] == self._data[7*line+column+1] and self._data[7*line+column+1] == self._data[7*line+column+2] and self._data[7*line+column+2] == self._data[7*line+column+3]
    #checks columns for a win
    def checkColumn(self,line,column):
        if line < 3 :
            return False
        return self._data[7*line+column] == self._data[7*(line -1)+column] and self._data[7*(line -1)+column] == self._data[7*(line -2)+column] and self._data[7*(line -2)+column] == self._data[7*(line -3)+column]
    #checks the principal diagonal for a win
    def checkDP(self,line,column):
        if line < 3 or column > 3:
            return False
        return self._data[7*line+column] == self._data[7*(line -1)+column+1] and self._data[7*(line -1)+column+1] == self._data[7*(line -2)+column+2] and self._data[7*(line -2)+column +2] == self._data[7*(line -3)+column+3]
    #checks the secondary diagonal for a win
    def checkDS(self,line,column):
        if column < 3 or line <3:
            return False
        return self._data[7*line + column] == self._data[7*(line -1)+column-1] and self._data[7*(line -1)+column-1] == self._data[7*(line -2)+column-2] and self._data[7*(line -2)+column-2] == self._data[7*(line -3)+column-3]


class test(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def test(self):
        b = board()
        b.move(1, "1")
        b.move(2,"1")
        b.move(3, "1")
        b.move(4, "1")
        assert b.win() == True
        
        