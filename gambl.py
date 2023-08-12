import random
import os

balance = 500


def menu(balance):
    os.system("clear")
    print ("WELCOME TO GAMBL!")
    print("MENU")
    print("(1) COINFLIP")
    menChoice = input()

    if menChoice == "1":
        coinflip(balance)
    else:
        print("Not a valid input")
        menu(balance)

def coinflip(balance):
    os.system("clear")
    print("COINFLIP")
    print()
    print("Balance", balance)
    print()


    coin = random.randint(0,1)

    coinflipBet = input("Bet amount: ")
    coinflipBet = int(coinflipBet)
    # converterar användarens bet till ett nummer 
    # annars sparas exempelvis bettet "20" som en string, vilket vi inte kan subtrahera eller addera sen när användaren vinner eller förlorar

    print()
    
    choise = input("Heads or tails? (h/t): ")
    if choise == "h":
        user = "Heads"
    elif choise == "t":
        user = "Tails"
    else:
        print ("Not a valid input!")
        coinflip(balance)

    if coin == 0:
        side = "Heads"
    else:
        side = "Tails"

    
    print("The coin lands on", side)
    print("")

    if user == side:
        print("You won!")
        balance += coinflipBet
    else:
        print ("You lost..")
        balance -= coinflipBet
    
    input("(ENTER to continue)")

    coinflip(balance)


menu(balance)