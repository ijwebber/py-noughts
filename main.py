
import display
import game
import user
import database as db

def newUser():
    display.clear()
    print("Create a new User:")
    name = input("Name: ")
    while db.checkUsernameExists(username):
        username = input("Username: ")
    #Check for existing username
    keyword = input("Keyword: ")
    input("New user created! Press enter to continue...")

def play():
    g = game.Game()
    while (g.isNotOver()):
        display.clear()
        display.board(g)
        g.takeTurn()
    input("Press enter to continue...")

def main():
    display.clear()
    option = display.menu()
    display.clear()
    if option == "0":
        print("Bye :(")
    elif option == "1":
        play()
        main()
    elif option == "2":
        newUser()
        main()
    else:
        input("Not a valid option, press enter to continue...")
        display.clear()
        main()

if __name__ == "__main__":
    main()