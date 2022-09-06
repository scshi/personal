import subprocess
import minecraft as mc
#4 subroutines

def theme(inputstart):
    again = 0
    while again == 0:
        print(inputstart + "******Theme******")
        
        #text colour
        print("""Pick a text colour: 
        0 = Black       8 = Gray
        1 = Blue        9 = Light Blue
        2 = Green       10 = Light Green
        3 = Aqua        11 = Light Aqua
        4 = Red         12 = Light Red
        5 = Purple      13 = Light Purple
        6 = Yellow      14 = Light Yellow
        7 = White       15 = Bright White
        (anything else will exit the theme maker)""")
        textcolour = int(input("Pick a colour: "))
        
        if textcolour > 15 or textcolour < 0:
            again = 1
        else:
            #background colour
            print("""Pick a text colour: 
            0 = Black       8 = Gray
            1 = Blue        9 = Light Blue
            2 = Green       10 = Light Green
            3 = Aqua        11 = Light Aqua
            4 = Red         12 = Light Red
            5 = Purple      13 = Light Purple
            6 = Yellow      14 = Light Yellow
            7 = White       15 = Bright White
            (anything else will reset the colour""")
            bgcolour = int(input("Pick a colour: "))
            
            #convert both text colour and bg colour to hexadecimal number to fit with command

            bgcolour = hex(bgcolour)
            textcolour = hex(textcolour)
            bgcolour = bgcolour.strip("0x")
            textcolour = textcolour.strip("0x")
            print(bgcolour)
            print(textcolour)

            #executing command in cmd prompt to change the colour

            text = 'cmd /k "color ' + str(bgcolour) + str(textcolour) + '"'
            subprocess.run(text, ["ls", "-l"] )

def bsearch():
    array = input("Enter the list of numbers separated by commas (,): ")
    array = array.split(",")
    spot = []
    searchfor = int(input("Enter the number you want to search for: "))
    count = 0
    found =  False
    print(str(len(array)))

    for i in range(len(array)):
        print(array[i])
        if searchfor == int(array[i]):
            count = count + 1
            found = True
            spot.append(i)
            print("found")
        else:
            print("not found yet")

    if found == False:
        print("The number" , str(searchfor) , "was not found")
    else:
        print("The number " , str(searchfor) , " was found " , str(count) , " time(s) at spot(s)" , str(spot) , ".")

def harshad(inputstart):
    num = str(input("Enter your number: "))
    total = 0
    for i in range(len(num)):
        total = total + int(num[i - 1])
    
    if int(num) % total == 0:
        print("This is a harshad number")
    else:
        print("This is not a harshad number")
    
def minecraft(inputstart, prefix):
    print(inputstart + "******MINECRAFT******")
    again = 0
    while again == 0:
        userinput = input(inputstart)
        if userinput == prefix + "effect":
            mc.effect(inputstart)
        elif userinput == prefix + "give":
            mc.give(inputstart)
        elif userinput == prefix + "ticktotime":
            mc.tickstotime(inputstart)
        elif userinput == prefix + "exit":
            again = 1