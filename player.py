class Player:

    def __init__(self, name, keyword):
        self.__name = name
        self.__keyword = keyword

    def getName(self):
        return self.__name
    
    def updateName(self, newName):
        self.__name = newName
    
    def checkKey(self, newKeyword):
        return (self.__keyword == newKeyword)

def main():
    pass

main()