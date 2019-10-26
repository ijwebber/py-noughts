import display

class Game:

    def __init__(self):
        self.__board = [[" ", " ", " "],
                        [" ", " ", " "],
                        [" ", " ", " "]]
        self.__players = ["X", "O"]
        self.__currentPlayer = 0
        self.__winner = ""

    def getBoard(self):
        return self.__board

    def getCurrentPlayer(self):
        return self.__players[self.__currentPlayer]

    def getOtherPlayer(self):
        return self.__players[abs(self.__currentPlayer - 1)]

    def isEmptySlot(self, x, y):
        if self.__board[y][x] == " ":
            return True
        else:
            return False

    def updateBoard(self, x, y):
        self.__board[y][x] = self.__players[self.__currentPlayer]
        self.__incrementCurrentPlayer()
    
    def __incrementCurrentPlayer(self):
        self.__currentPlayer = abs(self.__currentPlayer - 1)

    def __checkForWinner(self):
        b = self.__board
        #Vertical
        i = 0
        for i in range(0,3):
            if b[0][i] == b[1][i] and b[1][i] == b[2][i] and b[0][i] != " ":
                self.__winner = b[0][i]
                return True

        #Horizontal
        i = 0
        for i in range(0,3):
            if b[i][0] == b[i][1] and b[i][1] == b[i][2] and b[i][0] != " ":
                self.__winner = b[i][0]
                return True
        
        #Diagonal

        return False

    def __checkForDraw(self):
        return False
    
    def isNotOver(self):
        if self.__checkForWinner():
            display.clear()
            display.board(self)
            print("Player " + self.__winner + " has won!")
            return False
        if self.__checkForDraw():
            return False
        return True
    
    def takeTurn(self):
        notValid = True
        while notValid:
            try:
                x = int(input("x: "))
                if x > 2 or x < 0:
                    raise Exception
                y = int(input("y: "))
                if y > 2 or y < 0:
                    raise Exception
                if self.isEmptySlot(x,y):
                    self.updateBoard(x,y)
                    notValid = False
                else:
                    print("Invalid Move: The box is not empty")
            except:
                print("Invalid Entry: You did not enter a valid input")

        
            
