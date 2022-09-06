import calculate as c
import currency as cc
def help():
    print("""******HELP******
    (prefix)exit       - closes exits the console
    (prefix)help       - Opens this list
    (prefix)pokemon    - Opens pokedex
    (prefix)calculator - opens the calculator
    (prefix)genshin    - opens the genshin info pages""")

def calculator(inputstart, prefix):
    print(inputstart + "******CALCULATOR******")
    again = 0
    while again == 0:
        userinput = input(inputstart)
        if userinput == prefix + "add":
            c.add(inputstart)
        elif userinput == prefix + "multiply":
            c.multiply(inputstart)
        elif userinput == prefix + "divide":
            c.divide(inputstart)
        elif userinput == prefix + "mod":
            c.mod(inputstart)
        elif userinput == prefix + "exit":
            again = 1

def currencies(inputstart, prefix):
    print(inputstart + "******REALTIME CURRENCY******")
    again = 0
    while again == 0:
        cc.choice(inputstart)

