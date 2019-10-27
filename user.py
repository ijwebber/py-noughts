import display

class User:

    def __init__(self, name, keyword, username):
        self.__name = name
        self.__keyword = keyword
        self.__username = username

    #Getters
    def getName(self):
        return self.__name
    
    def getUsername(self):
        return self.__username
        
    #Setters
    def setName(self, newName):
        self.__name = newName
    
    def setUsername(self, newUsername):
        self.__username = newUsername
    
    #Methods
    def checkKey(self, newKeyword):
        return (self.__keyword == newKeyword)