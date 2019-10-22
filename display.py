def menu():
    print("1. New Game\n2. Create New Player\n3. Update Player\n4. View Player Stats\n5. Delete Player")
    return (input("Option: "))

def clear():
    i = 0
    for i in range(0, 100):
        print("\n")