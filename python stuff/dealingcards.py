import random

deck = ["♤ : 1", "♤ : 2", "♤ : 3", "♤ : 4", "♤ : 5", "♤ : 6", "♤ : 7", "♤ : 8", "♤ : 9", "♤ : 10", "♤ : 11", "♤ : 12", ""]
usedlist = []
p1 = []
ValueExist = 0 #used numbers to replace bool: 0 - Start the first while loop, 1 - True, 2 - False
i = 0

#draws 12 cards
for i in range(12):#
    ValueExist = 0
    while ValueExist == 0:  #makes sure that there is one value added each time
        gennum = random.randint(1, 12)
        print(gennum)  
        #checks to see if gennum is in usedlist
        for i in range(len(usedlist)):
            if gennum == usedlist[i]:
                #if the value is found then the check is stopped and the while loop is repeated
                print("found")
                ValueExist = 1
            else:
                print("not found")
                i = i + 1
        if ValueExist == 0:
            ValueExist = 1
            usedlist.append(gennum)
            p1.append(deck[gennum - 1])
            print("not found at all")
        elif ValueExist == 1:
            ValueExist = 0

print(p1)
print(usedlist)