import random
import os

balance = 500


def menu(balance):
    os.system("clear")
    print ("WELCOME TO GAMBL!")
    print("MENU")
    print("(1) COINFLIP")
    print("")
    print("If you want to go back at any time, type 'x' when presented with an input")
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
    if coinflipBet == "x":
        menu(balance)
    else:
        coinflipBet = int(coinflipBet)
        # converts the users bet input to and integer

    if coinflipBet > balance:
        print("You are trying to bet money that you dont have, maybe take a loan? ;)")
        input("(ENTER to continue)")
        coinflip(balance)



    print()
    
    choise = input("Heads or tails? (h/t): ")
    if choise == "h":
        guess = "Heads"
    elif choise == "t":
        guess = "Tails"
    elif choise == "x":
        menu(balance)
    else:
        print ("Not a valid input!")
        coinflip(balance)

    if coin == 0:
        side = "Heads"
    else:
        side = "Tails"

    
    print("The coin lands on", side)
    print("")

    if guess == side:
        print("You won!")
        balance += coinflipBet
    else:
        print ("You lost..")
        balance -= coinflipBet
    
    input("(ENTER to continue)")

    if balance == 0:
        bankrupt(balance)
    else:
        coinflip(balance)

    

def bankrupt(balance):
    os.system("clear")
    print("GAME OVER")
    print("You have lost all of your money")
    print()
    input("ENTER to exit game")
    exit()

menu(balance)
