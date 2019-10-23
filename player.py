class Player:

    def __init__(self, name, keyword, username, guest):
        self.__name = name
        self.__keyword = keyword
        self.__username = username
        self.__guest = guest

    #Getters
    def getName(self):
        return self.__name
    
    def getUsername(self):
        return self.__username

    def isGuest(self):
        return self.__guest
        
    #Setters
    def setName(self, newName):
        self.__name = newName
    
    def setUsername(self, newUsername):
        self.__username = newUsername
    
    def checkKey(self, newKeyword):
        return (self.__keyword == newKeyword)

def main():
    pass

main()