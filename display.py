import game

def menu():
    print("0. Exit\n1. New Game")#\n2. Create New Player\n3. Update Player\n4. View Player Stats\n5. Delete Player")
    return input("Option: ")

def clear():
    i = 0
    for i in range(0, 100):
        print("\n")

def board(g):
    print("Player", g.getCurrentPlayer(), "<-----")
    print("Player", g.getOtherPlayer(),"\n")
    
    print("  0   1   2  x")
    i = 0
    a = g.getBoard()
    for i in range(len(a)):
        print(str(i), a[i][0], "|", a[i][1], "|", a[i][2])
    print("y\n")

