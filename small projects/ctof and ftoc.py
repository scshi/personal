def ctof():
    c = int(input("Enter the temperature in degrees celsius: "))
    f = (c * 9/5) + 32
    print("The temperature: " + str(c) + " in degrees celsius is " + str(f) + " fahrenheit")

def ftoc():
    f = int(input("Enter the temperature in fahrenheit: "))
    c = (f - 32) * 5/9
    print("the temperature: " + str(f) + " in fahrenheit is " + str(c) + " degrees celsius")

def kgtolb():
    kg = int(input("Enter the weight in KG: "))
    lb = kg * 2.205
    print("The Weight: " + str(kg) + " in Kilograms is " + str(lb) + " in pounds")

def lbtokg():
    lb = int(input("Enter the weight in LB: "))
    kg = lb / 2.205
    print("The Weight: " + str(lb) + " in Pounds is " + str(kg) + " in kilograms")

#this is the main code
again = 'y'
menu = int(input("""Choose which one you want to pick:
    1. celsius to fahrenheit
    2. fahrenheit to celsius
    3. Kilos to pounds
    4. Pounds to kilos"""))

while again == 'y':
    if menu == 1:
        ctof()
    elif menu == 2:
        ftoc()
    elif menu == 3:
        kgtolb()
    elif menu == 4:
        lbtokg()
    else:
        again = "l"
