import random
#4 subroutines
"""
def drawcards(inputstart):
    deck = ["♤ : 1", "♤ : 2", "♤ : 3", "♤ : 4", "♤ : 5", "♤ : 6", "♤ : 7", "♤ : 8", "♤ : 9", "♤ : 10", "♤ : 11", "♤ : 12", "♤ : 13", "♡ : 1", "♡ : 2", "♡ : 3", "♡ : 4", "♡ : 5", "♡ : 6", "♡ : 7", "♡ : 8", "♡ : 9", "♡ : 10", "♡ : 11", "♡ : 12", "♡ : 13", "♧ : 1", "♧ : 2", "♧ : 3", "♧ : 4", "♧ : 5", "♧ : 6", "♧ : 7", "♧ : 8", "♧ : 9", "♧ : 10", "♧ : 11", "♧ : 12", "♧ : 13", "⋄ : 1", "⋄ : 2", "⋄ : 3", "⋄ : 4", "⋄ : 5", "⋄ : 6", "⋄ : 7", "⋄ : 8", "⋄ : 9", "⋄ : 10", "⋄ : 11", "⋄ : 12", "⋄ : 13"]
    print(len(deck))
    usedlist = []
    p1 = []
    ValueExist = 0 #used numbers to replace bool: 0 - Start the first while loop, 1 - True, 2 - False
    i = 0
    amount = 12894198759287359
    while amount > 52:
        amount = int(input(inputstart + "How many cards do you want to draw: "))
        if amount > 52:
            print("Number is too high. pls try again")

    #draws 12 cards
    for i in range(amount):#
        ValueExist = 0
        while ValueExist == 0:  #makes sure that there is one value added each time
            gennum = random.randint(1, len(deck))
            print(gennum)  
            #checks to see if gennum is in usedlist
            for i in range(len(usedlist)):
                if gennum == usedlist[i]:
                    #if the value is found then the check is stopped and the while loop is repeated
                    ValueExist = 1
                else:
                    i = i + 1
            if ValueExist == 0:
                ValueExist = 1
                usedlist.append(gennum)
                p1.append(deck[gennum - 1])
            elif ValueExist == 1:
                ValueExist = 0

    print(p1)

def drawcards2(inputstart):
    deck = ["♤ : 1", "♤ : 2", "♤ : 3", "♤ : 4", "♤ : 5", "♤ : 6", "♤ : 7", "♤ : 8", "♤ : 9", "♤ : 10", "♤ : 11", "♤ : 12", "♤ : 13", "♡ : 1", "♡ : 2", "♡ : 3", "♡ : 4", "♡ : 5", "♡ : 6", "♡ : 7", "♡ : 8", "♡ : 9", "♡ : 10", "♡ : 11", "♡ : 12", "♡ : 13", "♧ : 1", "♧ : 2", "♧ : 3", "♧ : 4", "♧ : 5", "♧ : 6", "♧ : 7", "♧ : 8", "♧ : 9", "♧ : 10", "♧ : 11", "♧ : 12", "♧ : 13", "⋄ : 1", "⋄ : 2", "⋄ : 3", "⋄ : 4", "⋄ : 5", "⋄ : 6", "⋄ : 7", "⋄ : 8", "⋄ : 9", "⋄ : 10", "⋄ : 11", "⋄ : 12", "⋄ : 13"]
    print(len(deck))
    usedlist = []
    p1 = []
    p2 = []
    ValueExist = 0 #used numbers to replace bool: 0 - Start the first while loop, 1 - True, 2 - False
    i = 0
    amount = 1
    while amount > 26:
        amount = 2 * (int(input(inputstart + "How many cards do you want to draw for each person: ")))
        if amount > 26:
            print("Number is too high, please try again")

    #draws 12 cards
    for i in range(amount):#
        ValueExist = 0
        while ValueExist == 0:  #makes sure that there is one value added each time
            gennum = random.randint(1, len(deck))
            print(gennum)  
            #checks to see if gennum is in usedlist
            for i in range(len(usedlist)):
                if gennum == usedlist[i]:
                    #if the value is found then the check is stopped and the while loop is repeated
                    ValueExist = 1
                else:
                    i = i + 1
            if ValueExist == 0:
                ValueExist = 1
                usedlist.append(gennum)
                if i % 2 == 0:
                    p1.append(deck[gennum - 1])
                else:
                    p2.append(deck[gennum - 1])
            elif ValueExist == 1:
                ValueExist = 0

    print(p1)
    print(p2)

def drawcards3(inputstart):
    deck = ["♤ : 1", "♤ : 2", "♤ : 3", "♤ : 4", "♤ : 5", "♤ : 6", "♤ : 7", "♤ : 8", "♤ : 9", "♤ : 10", "♤ : 11", "♤ : 12", "♤ : 13", "♡ : 1", "♡ : 2", "♡ : 3", "♡ : 4", "♡ : 5", "♡ : 6", "♡ : 7", "♡ : 8", "♡ : 9", "♡ : 10", "♡ : 11", "♡ : 12", "♡ : 13", "♧ : 1", "♧ : 2", "♧ : 3", "♧ : 4", "♧ : 5", "♧ : 6", "♧ : 7", "♧ : 8", "♧ : 9", "♧ : 10", "♧ : 11", "♧ : 12", "♧ : 13", "⋄ : 1", "⋄ : 2", "⋄ : 3", "⋄ : 4", "⋄ : 5", "⋄ : 6", "⋄ : 7", "⋄ : 8", "⋄ : 9", "⋄ : 10", "⋄ : 11", "⋄ : 12", "⋄ : 13"]
    print(len(deck))
    usedlist = []
    p1 = []
    p2 = []
    p3 = []
    ValueExist = 0 #used numbers to replace bool: 0 - Start the first while loop, 1 - True, 2 - False
    i = 0
    amount = random.randint(17, 95178468516857419716975897164389576139857632984761856183658197658937518974365987698768768768768768768768768768768768)
    #makes sure that the amount doesnt go above 17
    while amount > 17:
        amount = (int(input(inputstart + "How many cards do you want to draw for each person: ")))
        if amount > 17:
            print("Number too high, try again")
    #draws 12 cards
    for i in range(amount * 3):#
        ValueExist = 0
        while ValueExist == 0:  #makes sure that there is one value added each time
            gennum = random.randint(1, len(deck))
            print(gennum)  
            #checks to see if gennum is in usedlist
            for i in range(len(usedlist)):
                if gennum == usedlist[i]:
                    #if the value is found then the check is stopped and the while loop is repeated
                    ValueExist = 1
                else:
                    i = i + 1
            if ValueExist == 0:
                ValueExist = 1
                usedlist.append(gennum)
                if i < amount:
                    p1.append(deck[gennum - 1])
                elif i < amount * 2:
                    p2.append(deck[gennum - 1])
                else:
                    p3.append(deck[gennum - 1])
            elif ValueExist == 1:
                ValueExist = 0

    print(p1)
    print(p2)
    print(p3) 

def drawcards4(inputstart):
    deck = ["♤ : 1", "♤ : 2", "♤ : 3", "♤ : 4", "♤ : 5", "♤ : 6", "♤ : 7", "♤ : 8", "♤ : 9", "♤ : 10", "♤ : 11", "♤ : 12", "♤ : 13",
    "♡ : 1", "♡ : 2", "♡ : 3", "♡ : 4", "♡ : 5", "♡ : 6", "♡ : 7", "♡ : 8", "♡ : 9", "♡ : 10", "♡ : 11", "♡ : 12", "♡ : 13", 
    "♧ : 1", "♧ : 2", "♧ : 3", "♧ : 4", "♧ : 5", "♧ : 6", "♧ : 7", "♧ : 8", "♧ : 9", "♧ : 10", "♧ : 11", "♧ : 12", "♧ : 13", 
    "⋄ : 1", "⋄ : 2", "⋄ : 3", "⋄ : 4", "⋄ : 5", "⋄ : 6", "⋄ : 7", "⋄ : 8", "⋄ : 9", "⋄ : 10", "⋄ : 11", "⋄ : 12", "⋄ : 13"]
    print(len(deck))
    usedlist = []
    p1 = []
    p2 = []
    p3 = []
    p4 = []
    ValueExist = 0 #used numbers to replace bool: 0 - Start the first while loop, 1 - True, 2 - False
    i = 0
    amount = 291847912848796519874658917698372698376483261598764618216587162875618265812678356821659876321847632897659821375819265387619853678
    #makes sure that the amount doesnt go above 17
    while amount > 13:
        amount = (int(input(inputstart + "How many cards do you want to draw for each person: ")))
        if amount > 13:
            print("Number too high, try again")
    #draws 12 cards
    for i in range(amount * 4):#
        ValueExist = 0
        while ValueExist == 0:  #makes sure that there is one value added each time
            gennum = random.randint(1, len(deck))
            print(gennum)  
            #checks to see if gennum is in usedlist
            for i in range(len(usedlist)):
                if gennum == usedlist[i]:
                    #if the value is found then the check is stopped and the while loop is repeated 
                    ValueExist = 1
                else:
                    i = i + 1
            if ValueExist == 0:
                ValueExist = 1
                usedlist.append(gennum)
                if i < amount:
                    p1.append(deck[gennum - 1])
                elif i < amount * 2:
                    p2.append(deck[gennum - 1])
                elif i < amount * 3:
                    p3.append(deck[gennum - 1])
                else:
                    p4.append(deck[gennum - 1])
            elif ValueExist == 1:
                ValueExist = 0
    print(p1)
    print(p2)
    print(p3)
    print(p4) 

               ###########
################blackjack################
               ###########

def startblackjack(usedlist, p1, p2, amount, p1num, p2num):
    deck = ["♤ : 1", "♤ : 2", "♤ : 3", "♤ : 4", "♤ : 5", "♤ : 6", "♤ : 7", "♤ : 8", "♤ : 9", "♤ : 10", "♤ : 11", "♤ : 12", "♤ : 13", "♡ : 1", "♡ : 2", "♡ : 3", "♡ : 4", "♡ : 5", "♡ : 6", "♡ : 7", "♡ : 8", "♡ : 9", "♡ : 10", "♡ : 11", "♡ : 12", "♡ : 13", "♧ : 1", "♧ : 2", "♧ : 3", "♧ : 4", "♧ : 5", "♧ : 6", "♧ : 7", "♧ : 8", "♧ : 9", "♧ : 10", "♧ : 11", "♧ : 12", "♧ : 13", "⋄ : 1", "⋄ : 2", "⋄ : 3", "⋄ : 4", "⋄ : 5", "⋄ : 6", "⋄ : 7", "⋄ : 8", "⋄ : 9", "⋄ : 10", "⋄ : 11", "⋄ : 12", "⋄ : 13"]
    ValueExist = 0 #used numbers to replace bool: 0 - Start the first while loop, 1 - True, 2 - False
    i = 0

    #draws 12 cards
    for i in range(amount):#
        ValueExist = 0
        while ValueExist == 0:  #makes sure that there is one value added each time
            gennum = random.randint(1, len(deck))
            print(gennum)  
            #checks to see if gennum is in usedlist
            for i in range(len(usedlist)):
                if gennum == usedlist[i]:
                    #if the value is found then the check is stopped and the while loop is repeated
                    ValueExist = 1
                else:
                    i = i + 1
            if ValueExist == 0:
                ValueExist = 1
                usedlist.append(gennum)
                if i % 2 == 0:
                    p1.append(deck[gennum - 1])
                    p1num.append(gennum - 1)
                else:
                    p2.append(deck[gennum - 1])
                    p2num.append(gennum - 1)
            elif ValueExist == 1:
                ValueExist = 0
    
    return usedlist, p1, p2

def stick_twist(usedlist, pdeck, amount, player, p1num, p2num):
    deck = ["♤ : 1", "♤ : 2", "♤ : 3", "♤ : 4", "♤ : 5", "♤ : 6", "♤ : 7", "♤ : 8", "♤ : 9", "♤ : 10", "♤ : 11", "♤ : 12", "♤ : 13", "♡ : 1", "♡ : 2", "♡ : 3", "♡ : 4", "♡ : 5", "♡ : 6", "♡ : 7", "♡ : 8", "♡ : 9", "♡ : 10", "♡ : 11", "♡ : 12", "♡ : 13", "♧ : 1", "♧ : 2", "♧ : 3", "♧ : 4", "♧ : 5", "♧ : 6", "♧ : 7", "♧ : 8", "♧ : 9", "♧ : 10", "♧ : 11", "♧ : 12", "♧ : 13", "⋄ : 1", "⋄ : 2", "⋄ : 3", "⋄ : 4", "⋄ : 5", "⋄ : 6", "⋄ : 7", "⋄ : 8", "⋄ : 9", "⋄ : 10", "⋄ : 11", "⋄ : 12", "⋄ : 13"]
    ValueExist = 0 #used numbers to replace bool: 0 - Start the first while loop, 1 - True, 2 - False
    i = 0
    
    #draws 12 cards
    for i in range(amount):#
        ValueExist = 0
        while ValueExist == 0:  #makes sure that there is one value added each time
            gennum = random.randint(1, len(deck))
            print(gennum)  
            #checks to see if gennum is in usedlist
            for i in range(len(usedlist)):
                if gennum == usedlist[i]:
                    #if the value is found then the check is stopped and the while loop is repeated
                    ValueExist = 1
                else:
                    i = i + 1
            if ValueExist == 0:
                ValueExist = 1
                usedlist.append(gennum)
                #assigns the card and number position to the player's array
                if player == 1:
                    pdeck.append(deck[gennum - 1])
                    p1num.append(gennum - 1)
            elif ValueExist == 1:
                ValueExist = 0
    
    return usedlist, player

def checkval(pnum):
    if (pnum <= 11 and pnum >= 13) or (pnum <= 24 and pnum >= 26):
        pnum = 11
    

def blackjack():
    again = 2
    usedlist = []
    p1 = []
    p2 = []
    #draws cards for base deck to play on
    amount = 4 
    carddecks = startblackjack(usedlist, p1, p2, amount)
    usedlist = carddecks[0]
    p1 = carddecks[1]
    p2 = carddecks[2]

    #makes a new variable to reset variables
    p1temp = []
    p2temp = []
    #choose whether to stick or twist

    while again > 0:
        choice = input("Stick or Twist: ")
        if again % 2 == 0:
            print("p1")
            if choice == "twist":
                #make a second deck that uses the 'usedlist' from the first deck and add them together
                twist = stick_twist(usedlist, [], 1, 1)
                print(twist)
                usedlist = usedlist + twist[0]
                p1 = p1 + twist[1]
                print(p1)
            elif choice != "twist":
                again = again + 1
        else:
            print("p2")
            if choice == "twist":
                #make a second deck that uses the 'usedlist' from the first deck and add them together
                twist = stick_twist(usedlist, [], 1, 2)
                print(twist)
                usedlist = usedlist + twist[0]
                p2 = p2 + twist[1]
                print(p2)
            elif choice != "twist":
                again = again + 1
    print(carddecks)
    print(p1)
    print(p2)
    print(usedlist)
 
#print all outputs


blackjack()
"""