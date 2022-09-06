kph_mph = str(input("Which one do you want to pick KPH or MPH: "))
numplate = str(input("What was the number plate: "))

numplate = numplate.replace(" ", "")
numplateage = numplate[2] + numplate[3]


if kph_mph.title() == "KPH":
    milebetween = int(input("Enter the distance between the two \ncameras in Kilometres: "))
else:
    milebetween = int(input("Enter the distance between the two \ncameras in miles: "))

if int(numplateage) > 50:
    numplateage = str((int(numplateage) - 50) + 2000)
else:
    numplateage = str(int(numplateage) + 2000)


timebetween = int(input("Enter the time it took in seconds: "))

milebetween = (milebetween/timebetween) * 360

print("The car with the numberplate: " + numplate + " was going " + str(int(milebetween)) + " " + kph_mph)
print("The car was also bought in: " + str(int(numplateage)))