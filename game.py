import display

class Game:

    def __init__(self):
        self.__board = [[" ", " ", " "],
                        [" ", " ", " "],
                        [" ", " ", " "]]
        self.__players = ["X", "O"]
        self.__currentPlayer = 0

    def getBoard(self):
        return self.__board

    def getCurrentPlayer(self):
        return self.__players[self.__currentPlayer]

    def getOtherPlayer(self):
        return self.__players[abs(self.__currentPlayer - 1)]

    def checkEmpty(self, x, y):
        if self.__board[y][x] == " ":
            return True
        else:
            return False

    def updateBoard(self, x, y):
        self.__board[y][x] = self.__players[self.__currentPlayer]
        self.__incrementCurrentPlayer()
    
    def __incrementCurrentPlayer(self):
        self.__currentPlayer = abs(self.__currentPlayer - 1)
    
    def isNotOver(self):
        return True