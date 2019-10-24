class Game:

    def __init__(self):
        self.__board = [[" ", " ", " "],
                        [" ", " ", " "],
                        [" ", " ", " "]]
        #self.__players = [p1, p2]
        self.__currentPlayer = 1

    def board(self):
        return self.__board

    def updateBoard(self, x, y):
        pass
