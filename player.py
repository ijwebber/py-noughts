class Player:

    def __init__(self, name, keyword):
        self.__name = name
        self.__keyword = keyword

    def getName(self):
        return self.__name
    
    def checkKey(self, newKeyword):
        return (self.__keyword == newKeyword)

def main():
    player1 = Player("Isaac", "capo")
    print(player1.getName())
    print(player1.checkKey("capo"))

main()