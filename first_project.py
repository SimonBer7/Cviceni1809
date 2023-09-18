
def get_num():

    x = input("Zadej cislo: ")
    y = int(x) + 1
    print(y)


running = True
while running:

    try:
        get_num()
        running = False
    except:
        print("Musite zadat cislo!")

