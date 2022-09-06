numplate = str(input("What was the number plate: "))

numplate = numplate.replace(" ", "")
numplateage = numplate[2] + numplate[3]

if int(numplateage) > 50:
    numplateage = str((int(numplateage) - 50) + 2000)
    print("You bought your car in " + numplateage + " \nin the period of 1 September "
     + numplateage + " and the end of February" + str(int(numplateage) + 1))
    print("Your number plate is " + numplate.title())
else:
    numplateage = str((int(numplateage) - 50) + 2000)
    print("You bought your car in " + numplateage + " \nin the period of 1 january "
     + numplateage + " and the end of August" + numplateage)
    print("Your number plate is " + numplate.title())
