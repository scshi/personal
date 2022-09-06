import random

def choice():
    menu = int(input("""******MENU******
    1) Draw Cards
    2) Higher or lower
    3) Specific house
    4) exit"""))
    return menu

def amountofcards():
    place = 'y'
    amountinput = int(input("How many cards do you want to draw? \n Answer here: "))

    while place == 'y':
        if amountinput > 52:
            amountinput = int(input("Number is not in range \n Try again:"))
        else:
            place = 'n'
            return amountinput

def spade(cardnum):
    cardnum2 = cardnum
    if cardnum2 == 11:
        cardnum2 = "Jack"
    elif cardnum2 == 12:
        cardnum2 = "Queen"
    elif cardnum2 == 13:
        cardnum2 = "King"
    else:
        cardnum2 = cardnum2
    return cardnum2

def club(cardnum):
    cardnum2 = cardnum
    if int(cardnum2 / 2) == 11:
        cardnum2 = "Jack"
    elif int(cardnum2 / 2) == 12:
        cardnum2 = "Queen"
    elif int(cardnum2 / 2) == 13:
        cardnum2 = "King"
    else:
        cardnum2 = str(int(cardnum2 / 2))
    return cardnum2

def heart(cardnum):
    cardnum2 = cardnum
    if int(cardnum2 / 3) == 11:
        cardnum2 = "Jack"
    elif int(cardnum2 / 3) == 12:
        cardnum2 = "Queen"
    elif int(cardnum2 / 3) == 13:
        cardnum2 = "King"
    else:
        cardnum2 = str(int(cardnum2 / 3))
    return cardnum2

def diamond(cardnum):
    cardnum2 = cardnum
    if int(cardnum2 / 4) == 11:
        cardnum2 = "Jack"
    elif int(cardnum2 / 4) == 12:
        cardnum2 = "Queen"
    elif int(cardnum2 / 4) == 13:
        cardnum2 = "King"
    else:
        cardnum2 = str(int(cardnum2 / 4))
    return cardnum2


def drawcards():
    again = 'y'
    rngtable = []
    amount = amountofcards()
    x = 0
    print(" Number ¦  Type ")
    print("--------¦-------")
    while again.title() == 'Y':
        while x <= amount:
            cardnum = random.randint(1,52)
            if cardnum not in rngtable:
                rngtable.append(cardnum)
                if cardnum <= 13:
                    cardnum2 = spade(cardnum)
                    print('{:^8}'.format(cardnum2)  + "¦" + '{:^8}'.format("Spades"))
                elif cardnum <= 26:
                    cardnum2 = club(cardnum)
                    print('{:^8}'.format(cardnum2)  + "¦" + '{:^8}'.format("Club"))
                elif cardnum <= 39:
                    cardnum2 = heart(cardnum)
                    print('{:^8}'.format(cardnum2)  + "¦" + '{:^8}'.format("Heart"))
                elif cardnum <= 52:
                    cardnum2 = diamond(cardnum)
                    print('{:^8}'.format(cardnum2)  + "¦" + '{:^8}'.format("Diamond"))
            else:
                cardnum = random.randint(1,52)
            x = x + 1
        again = input("Want to draw another pack (y or n): ")

def drawtypecard():
    amount = amountofcards()
    typeofcard = input("""What type of card do you want:
        (s) for Spades
        (c) for Clubs
        (h) for Hearts
        (d) for Diamonds""")
    if typeofcard.title() == "S":
        typeofcard = "Spades"
    elif typeofcard.title() == "C":
        typeofcard = "Clubs"
    elif typeofcard.title() == "H":
        typeofcard = "Hearts"
    elif typeofcard.title() == "D":
        typeofcard = "Diamonds"
    again = 0
    while again <= amount:
        rng = random.randint(1, 13)
        if rng == 11:
            print('{:^8}'.format("Jack")  + "¦" + '{:^8}'.format(typeofcard))
        elif rng == 12:
            print('{:^8}'.format("Queen")  + "¦" + '{:^8}'.format(typeofcard))
        elif rng == 13:
            print('{:^8}'.format("King")  + "¦" + '{:^8}'.format(typeofcard))
        else:
            print('{:^8}'.format(str(rng))  + "¦" + '{:^8}'.format(typeofcard))
        again = again + 1
    return 0

def higherorlower():
    again = 'y'
    while again.title() == 'Y':
        firstcardnum = random.randint(1,13)
        secondcardnum = random.randint(1,13)

        if secondcardnum == firstcardnum:
            secondcardnum = random.randint(1,13)
        if firstcardnum == 1:
            choice = input("The card is: Ace \n Higher or Lower (H or L): ")
        elif firstcardnum == 11:
            choice = input("The card is: Jack \n Higher or Lower (H or L): ")
        elif firstcardnum == 12:
            choice = input("The card is: Queen \n Higher or Lower (H or L): ")
        elif firstcardnum == 13:
            choice = input("The card is: King \n Higher or Lower (H or L): ")
        else:
            choice = input("The card is: " + str(firstcardnum) + " \n Higher or Lower (H or L): ")
        if choice.title() == "H" and firstcardnum < secondcardnum:
            print("Correct")
        elif choice.title() == "L" and firstcardnum > secondcardnum:
            print("Correct")
        else:
            print("Incorrect")
        again = input("Do you want to continue? (y or n)")

#main code
cards = {}
again = 'y'
while again == 'y':
    choicenum = choice() #chooses what thing you want to do
    if choicenum == 1:
        drawcards() #draws the cards
    elif choicenum == 2:
        higherorlower()
    elif choicenum == 3:
        drawtypecard()
    else:
        again = "NOOOOOOOOOOOOOOOO I REFUSE"

