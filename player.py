import display

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

def getPlayers():
    i = 0
    for i in range(0,2):
        option = int(input("Player " + str(i+1) + "\n1. Search for player\n2. Play as a guest\nOption: "))
        if option == 1:
            pass
            #enter username
            #player.checkExists
        elif option == 2:
            pass
        else:
            input("Not a valid option, press enter to continue...")
            display.clear()
            getPlayers()
        display.clear()

def main():
    pass

main()