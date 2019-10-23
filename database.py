import sqlite3
import player

class Database:

    def __init__(self):
        pass

    def getPlayer(self):
        #Will look up a player and return the player object from info from the database
        return player.Player("Isaac", "capo")