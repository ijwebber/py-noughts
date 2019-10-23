
import display
import player
import game

def main():
    option = display.menu()
    display.clear()
    if option == "1":
        pass
        #game.new()
    elif option == "2":
        pass
        #player.new()
    elif option == "3":
        pass
        #player.update()
    elif option == "4":
        pass
        #player.stats()
    elif option == "5":
        pass
        #player.delete()
    else:
        input("Not a correct option, press enter to continue...")
        display.clear()
        main()
    
    g = game.Game()
    display.game(g.board())

main()