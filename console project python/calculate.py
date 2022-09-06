def add(inputstart):
    print(inputstart + "******ADDITION******")
    again = 0
    while again == 0:
        try:
            no_of_numbers = int(input(inputstart + "How many numbers do you want to add: "))
            total = 0
            for i in range(no_of_numbers):
                num = int(input(inputstart + "Enter a number: "))
                total = total + num
            print(inputstart + "The total is: " + str(total))
            again = 1
        except ValueError:
            print("Please enter a number")

def multiply(inputstart):
    print(inputstart + "******MULTIPLICATION******")
    again = 0
    while again == 0:
        try:
            no_of_numbers = int(input(inputstart + "How many numbers do you want to multiply: "))
            total = 0
            for i in range(no_of_numbers):
                num = int(input(inputstart + "Enter a number: "))
                total = total * num
            print(inputstart + "The total is: " + str(total))
            again = 1
        except ValueError:
            print("Please enter a number")

def divide(inputstart):
    print(inputstart + "******DIVISION******")
    again = 0
    while again == 0:
        try:
            answer = 0
            num1 = int(input(inputstart + "Enter number 1: "))
            num2 = int(input(inputstart + "Enter number 2: "))
            answer = num1 / num2
            print(inputstart + "The answer: " + str(answer))
        except ValueError:
            print("Please enter a number")

def mod(inputstart):
    print(inputstart + "******MODULUS******")
    again = 0
    while again == 0:
        try:
            answer = 0
            num1 = int(input(inputstart + "Enter number 1: "))
            num2 = int(input(inputstart + "Enter number 2: "))
            answer = num1 % num2
            print(inputstart + "The remainder is: " + str(answer))
        except ValueError:
            print("Please enter a number")

def percentage(inputstart):
    print(inputstart + "******MODULUS******")
    again = 0
    while again == 0:
        try:
            answer = 0
            num1 = int(input(inputstart + enter ))

def average():
    num = ''
    numarray = []
    counter = 0 
    total = 0
    avg = 0
    while num != 'x':
        print("******HINT****** \n If you want to stop just type 'x'")
        try:
            num = input("Enter the number you want to enter: ")
            if num != 'x':
                numarray = numarray.append(int(num))
        except ValueError:
            print("Please enter an actual number")
        counter = counter + 1
    for i in len(numarray):
        total = total + numarray[i - 1]
        avg = total / counter - 1
