import random

print("Welcome to the national quiz of math")
name = input("What is your name: ")
print("Hello, " + name)

question1_1 = random.randint(0,10)
question1_2 = random.randint(0,10)
answer = question1_1 + question1_2
response = int(input("What is " + str(question1_1) + " + " + str(question1_2) + ": "))
if response == answer:
    print("You are correct!!!")
else:
    print("Sry your wrong")

question2_1 = random.randint(0,10)
question2_2 = random.randint(0,10)
answer = question2_1 * question2_2
response = int(input("What is " + str(question2_1) + " X " + str(question2_2) + ": "))
if response == answer:
    print("You are correct!!!")
else:
    print("Sry your wrong")

question3_1 = random.randint(1,10)
question3_2 = random.randint(1,10)
answer = round(question3_1 / question3_2, 1)
response = input("What is " + str(question3_1) + " / " + str(question3_2) + ": ")
if response == answer:
    print("You are correct!!!")
else:
    print("Sry your wrong" + str(answer))