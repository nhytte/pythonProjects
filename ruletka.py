import random
import os

balance = 1000
choice = 2
jeszcze = 2


# ruleta
def ruletka():
    global balance
    print("Wybierz kolor: czerwony/czarny/zielony")
    color = input()
    print("Twoja stawka")
    bid = int(input())
    balance -= bid
    print("\n")
    win = 0
    x = int(random.randrange(1,51))
    if color == "czerwony":
        if x in range(1,25):
            balance += bid*2
            howMuch = bid*2
            win = 1
    if color == "czarny":
        if x in range(25,49):
            balance += bid*2
            howMuch = bid * 2
            win = 1
    if color == "zielony":
        if x in range(49,51):
            balance += bid*14
            howMuch = bid * 14
            win = 1
    if win == 1:
        print("Wygrałeś: ", howMuch, "\n Twój balans: ", balance)
    else:
        print("Przegrałeś: ", bid)
    print(x)

# MENU
while jeszcze == 2:
    print("Witaj w nhyte's Casino")
    print("Twój balans konta wynosi: ", balance)

    print("\nWybierz jedną z opcji:")
    print("1. Zakręć")
    print("2. Zamknij")
    choice = int(input())

    if choice == 1:
        ruletka()
        input()
        os.system('cls')
    elif choice == 2:
        jeszcze = 1






