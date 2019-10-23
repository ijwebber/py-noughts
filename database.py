import sqlite3
import player

class Database:

    def __init__(self):
        pass

    def getPlayer(self, username):
        #Will look up a player and return the player object from info from the database
        return player.Player("Isaac", "capo", username)
    
    def newPlayer(self, player):
        pass
        #with sqlite3.connect("db.db") as db:

    def checkPlayerExists(self, username):
        with sqlite3.connect("db.db") as db:
            cursor = db.cursor()
            Variable = username
            cursor.execute("select username from Players where Username=?", (Variable,))
            select = cursor.fetchall()
        if select:
            print("User exists")
        else:
            print("User does not exist")
        

def main():
    data = Database()
    data.checkPlayerExists("ijwebber")

main()