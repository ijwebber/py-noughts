
import display
import game

def play():
    g = game.Game()
    while (g.isNotOver()):
        display.clear()
        display.board(g)
        input("x: ")
        input("y: ")


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