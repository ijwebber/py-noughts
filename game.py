class Game:

    def __init__(self, p1, p2):
        self.__board = [[" ", " ", " "],
                        [" ", " ", " "],
                        [" ", " ", " "]]
        self.__players = [p1, p2]
        self.__currentPlayer = 0

    def board(self):
        return self.__board

    def updateBoard(self, x, y):
        pass
