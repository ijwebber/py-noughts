
import display
import player
import game

def play():
    g = game.Game()

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