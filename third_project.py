from math import sqrt

running = True
while running:
    try:
        L = int(input("Zadej indukcnost [H]:"))
        running = False
    except:
        print("Zadej cislo!")


try:
    C = int(input("Zadej kapacitu [F]:"))
    if C > 0:
        F = 1 / (2 * 3.14 * sqrt(int(L) * int(C)))
        print("Frekvence je: " + str(F) + "Hz")
    else:
        raise Exception
except:
    print("Neco je spatne!")

