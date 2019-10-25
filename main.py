
import display
import game

def play():
    while (game.isNotOver()):
        pass

def main():
    option = display.menu()
    display.clear()
    if option == 1:
        play()
    else:
        input("Not a valid option, press enter to continue...")
        display.clear()
        main()

main()