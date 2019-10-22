def menu():
    print("1. New Game\n2. Create New Player\n3. View Stats")
    return (input("Option: "))

def clear():
    i = 0
    for i in range(0, 100):
        print("\n")