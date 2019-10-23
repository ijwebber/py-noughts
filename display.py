def menu():
    print("1. New Game\n2. Create New Player\n3. Update Player\n4. View Player Stats\n5. Delete Player")
    return (int(input("Option: ")))

def clear():
    i = 0
    for i in range(0, 100):
        print("\n")

def game(a):
    i = 0
    for i in range(len(a)):
        print(a[i][0], "|", a[i][1], "|", a[i][2])

