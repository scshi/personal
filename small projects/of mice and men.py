import random

num = str(random.randint(0,9999))
print(num)
numinp = input("Guess the number: ")
mice = 0
man = 0


for i in range(0,4):
    if int(num[i-1]) == int(numinp[i-1]):
        print(num[i-1])
        print(numinp[i-1])
        mice = mice + 1
        print("Mouse")
    elif int(num[i-1]) != int(numinp[i-1]):
        print(num[i-1])
        print(numinp[i-1])
        man = man + 1
        print("Man")

print("You had " + str(mice) + " Mice and " + str(man) +" men")
