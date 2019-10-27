import sqlite3
import user

class Database:

    def __init__(self):
        pass

    def getuser(self, username):
        #Will look up a user and return the user object from info from the database
        return user.user("Isaac", "capo", username)
    
    def newuser(self, user):
        pass
        #with sqlite3.connect("db.db") as db:

    def checkuserExists(self, username):
        with sqlite3.connect("db.db") as db:
            cursor = db.cursor()
            Variable = username
            cursor.execute("select username from users where Username=?", (Variable,))
            select = cursor.fetchall()
        if select:
            print("User exists")
        else:
            print("User does not exist")
        

def main():
    data = Database()
    data.checkuserExists("ijwebber")

main()