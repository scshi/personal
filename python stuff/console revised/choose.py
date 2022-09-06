import cmd
import calculate as c
import currency as cc
import misc as ms
import cards as ca
import os
#6 subroutines

def help():
    print("""******HELP******
    (prefix)exit       - closes or exits the console
    (prefix)help       - Opens this list
    (prefix)pokemon    - Opens pokedex
    (prefix)calculator - opens the calculator (iteration not fixed, will be fixed in version 4)
    (prefix)misc       - miscellaneous things""")

def currencies(inputstart):
    print(inputstart + "******CURRENCY******")
    again = 1
    while again == 1:
        currency = input(inputstart + " Enter the shorthand for the starting currency: ").upper()
        choose = int(input("""******MENU******
        1. See the conversion rate from starting currency
        2. Convert from one currency to another
        3+. Exit
        Enter here: """))
        if choose == 1:
            cc.convertrate(inputstart, currency)
        elif choose == 2:
            cc.convertion(inputstart, currency)
        else:
            again = 0

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
        elif userinput == prefix + "average":
            c.average(inputstart)
        elif userinput == prefix + "percent":
            c.percent(inputstart)
        elif userinput == prefix + "exit":
            again = 1

def misc(inputstart,prefix):
    print(inputstart + "******Miscellanaeous******")
    again = 0
    placeholder = 0
    while again == 0:
        userinput = input(inputstart)
        if userinput == prefix + "theme":
            ms.theme(inputstart)
        elif userinput == prefix + "bsearch" or userinput == prefix + "binarysearch":
            ms.bsearch()
        elif userinput == prefix + "minecraft":
            ms.minecraft(inputstart)
        elif userinput == prefix + "exit":
            again = 1

def cards(inputstart,prefix):
    print(inputstart + "******Cards*******")
    again = 0
    while again == 0:
        userinput = input("""1. Draw cards for one person
        2. Draw cards for two people
        3. Draw cards for three people
        4. Draw cards for four people
        5. Exit""")
        if userinput == "1":
            ca.drawcards(inputstart)
        elif userinput == "2":
            ca.drawcards2(inputstart)
        elif userinput == "3":
            ca.drawcards3(inputstart)
        elif userinput == "4":
            ca.drawcards4(inputstart)
        else:
            again = 1


def date(inputstart):
    os.system('cmd /k "date"')