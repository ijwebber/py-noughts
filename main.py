
import display
import player
import game

def findPlayer():
    option = int(input("Player 1\n1. Search for player\n2. Play as a guest\nOption: "))
    if option == 1:
        pass
        #enter username
        #player.checkExists
    elif option == 2:
        pass
    else:
        input("Not a valid option, press enter to continue...")
        display.clear()
        findPlayer()


def main():
    option = display.menu()
    display.clear()
    if option == 1:
        findPlayer()
        pass
        #choose player from list 
        #game.new()
    elif option == 2:
        pass
        #player.new()
    elif option == 3:
        pass
        #player.update()
    elif option == 4:
        pass
        #player.stats()
    elif option == 5:
        pass
        #player.delete()
    else:
        input("Not a valid option, press enter to continue...")
        display.clear()
        main()

main()