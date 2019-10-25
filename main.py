
import display
import game

def play():
    g = game.Game()
    while (g.isNotOver()):
        display.clear()
        display.board(g)
        g.takeTurn()
        input()
    #Draw Win Lose 



def main():
    option = display.menu()
    display.clear()
    if option == "1":
        play()
    else:
        input("Not a valid option, press enter to continue...")
        display.clear()
        main()

main()