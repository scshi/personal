import choose as h
#one subroutine (29 subroutines in total from all files)

def menumain(inputstart, prefix):
    print(inputstart + "******MAIN******")
    again = 0
    while again == 0:
        userinput = input(inputstart)
        if userinput == prefix + "exit":
            again = 1
        elif userinput == prefix + "help":
            h.help()
        elif userinput == prefix + "calculator":
            h.calculator(inputstart, prefix)
        elif userinput == prefix + "currency":
            h.currencies(inputstart)
        elif userinput == prefix + "Genshin":
            h.genshin(inputstart, prefix)
        elif userinput == prefix + "misc":
            h.misc(inputstart, prefix)
        elif userinput == prefix + "date":
            h.date(inputstart)
        elif userinput == prefix + "cards":
            h.cards(inputstart, prefix)
        elif userinput == prefix + "dadfunny":
            num = int(input("Enter a number: "))
            if num <= 198479187564897651987689768687438765837658376548736587436587364857638475683476587346587346857638475687346587346856348756834658347568768768753628764023846023762837658947652897659843275698765873465897432659874528973429874892376548376:
                print("dad is still not funny")
            else:
                print("Dad has outdated humour and is really embarrassing to be around")


print("CONSOLE > ******CONSOLE******")
user = input("Enter your name: ")
inputstart = "CONSOLE/" + user + " > "
prefix = input("What prefix do you want (e.g. /, ?, .): ")
menumain(inputstart, prefix)