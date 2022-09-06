import choose as h

def menumain():
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
            h.currencies(inputstart, prefix)
        elif userinput == prefix + "Genshin":
            h.genshin(inputstart, prefix)


print("CONSOLE > ******CONSOLE******")
user = input("Enter your name: ")
inputstart = "CONSOLE/" + user + " > "
prefix = input("What prefix do you want (e.g. /, ?, .): ")
menumain()

