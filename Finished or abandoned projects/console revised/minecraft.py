#3 subroutines

def effect():
    again = 0
    while again == 0:
        person = input("Who do you want to give the effect to (me/someone/everyone/nearby): ")
        if person.lower() == "me": #assigns the player itself
            person = "@s"
            again = 1
        elif person.lower() == "someone": #assigns the ign of the person they want to effect
            person = input("What is the IGN of the person you want to give: ")
            again = 1
        elif person.lower() == "everyone": #assigns '@a' if give to everyone
            person = "@a"
            again = 1
        elif person.lower() == "nearby": #assigns '@p' if give to nearest person
            person = "@p"
            again = 1
        else:
            print("Sorry try again (look inside the brackets in the question)")

    #type of potion
    again = 0
    while again == 0:
        effect = input("What effect do you want to give: ")
        if effect != " " or effect != "":
            command = "/effect give " + person + " " + effect.lower()
            again = 1
        else:
            effect = input("What effect do you want to give: ")
    
    #time of potion
    again = 0
    while again == 0:
        time = input("How long do you want the effect to last (infinite/(seconds)): ")
        if time == "infinite" or int(time) > 9999999:
            time  = "9999999"
            again = 1
        elif time == "30":
            time = ""
            again = 1
        elif time != "":
            again = 1

    command = command + " " + time

    
    print("The command line is shown below: \n ")
    print(command)

def give():
    bori = input("Which do you want to give: \n 1. Block \n 2. Item ")
    #decides whether to give a block or item
    if bori == 1: 
        bori = "block"
    elif bori == 2:
        bori = "item"
    again = 0
    while again == 0:
        person = input("Who do you want to give the " + bori + " to (me/someone/everyone/nearby): ") #asks who to give the block/item to
        if person.lower() == "me": #assigns the player itself
            person = "@s"
            again = 1
        elif person.lower() == "someone": #assigns the ign of the person they want to effect
            person = input("What is the IGN of the person you want to give: ")
            again = 1
        elif person.lower() == "everyone": #assigns '@a' if give to everyone
            person = "@a"
            again = 1
        elif person.lower() == "nearby": #assigns '@p' if give to nearest person
            person = "@p"
            again = 1
        else:
            print("Sorry try again (look inside the brackets in the question)")
        
    again = 0 #adds the correct item or block needed
    while again == 0:
        block = input("What " + bori + " do you want to give: ")
        block = block.replace(' ', '_')
        if block != "_" or block != "":
            command = "/give " + person + " minecraft:" + effect.lower()
            again = 1
    
    again = 0 #adds the amount of blocks if the requested give command contains blocks
    while bori == "block" and again == 0:
        amount = input("How much of block: " + block + ", do you want to give:")
        if amount != 0:
            command = command + " " + amount
            again = 1
    
    print("The command line is shown below \n")
    print(command)


def tickstotime():
    ticks = int(input("How many ticks: "))
    #calculates the remainder of seconds and assigns minutes to use later
    seconds = ticks / 20 
    minutes = seconds
    seconds = seconds % 60 
    #calculates the amount of minutes
    minutes = minutes - seconds
    minutes = minutes / 60
    #calculates the amount of hours
    hours = minutes / 60
    
    if hours >= 1:
        minutes = minutes - (minutes % 60) #find the remainding minutes
        print(str(ticks) + " ticks is " + str(hours) + " hours " + str(minutes) + " minutes " + str(seconds) + " Seconds.") # Output
    elif minutes >= 1:
        print(str(ticks) + " ticks is " + str(minutes) + " minutes " + str(seconds) + " Seconds.") # Output
    elif seconds >= 1:
        print(str(ticks) + " ticks is " + str(seconds) + " Seconds.") # Output
    else:
        print("Too small a number.")

