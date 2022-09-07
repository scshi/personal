import area as a
#8 subroutines (6 functional)
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
            again = 1
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
            again = 1
        except ValueError:
            print("Please enter a number")

def percent(inputstart):
    print(inputstart + "******PERCENTAGES******")
    again = 0
    while again == 0:
        try:
            answer = 0
            num1 = int(input(inputstart + "Enter number 1: "))
            num2 = int(input(inputstart + "Enter number 2: "))
            percentage = (num2 / num1) * 100
            print(inputstart , str(num2) + " is " + str(percentage) + " of " + str(num1))
            again = 1
        except ValueError:
            print("Please enter a number")

def three_d_area(inputstart):
    print(inputstart + "******VOLUME******")
    again = 0
    while again == 0:
        choice = int(input("""Choose which shape you want to see the Volume of: 
        1. Cuboid
        2. Pyramid
        3. Sphere
        4. Sector"""))
        if choice == 1:
            a.vcuboid(inputstart)
        elif choice == 2:
            a.rectangle(inputstart)
        elif choice == 3:
            a.sphere(inputstart)
        elif choice == 4:
            a.sector(inputstart)

def _2Darea(inputstart):
    print(inputstart + " ******VOLUME******")
    again = 0
    while again == 0:
        choice = int(input("""Choose which shape you want to see the area of: 
        1. Triangle
        2. Rectangle
        3. Circle
        4. Sector"""))
        if choice == 1:
            a.triangle(inputstart)
        elif choice == 2:
            a.rectangle(inputstart)
        elif choice == 3:
            a.circle(inputstart)
        elif choice == 4:
            a.sector(inputstart)
            

#not done yet
"""
def iteration(inputstart):
    print(inputstart + "******ITERATION******")
    again = 0
    while again == 0:
        choice = int(input(""""""Choose which equation you want to see the final solution: 
        1. T(n+1) = A(n) (operand) B 
        2. T(n+1) = (A(n) (operand) B) / C""""""))
        n = int(input("What do you want the starting number to be: "))
        if choice == 1:
            iteration1(inputstart, n)


# not done yet
def iteration1(inputstart, n):
    print(inputstart + "******ITERATION******")
    again = 0
    while again == 0:
        operand = input("Which operand do you want to use (T(n+1) = A(n) (operand) B): ")#gets the right operand needed for operation
        #verification of operand
        if operand == "x" or operand == "*" or operand == "+" or operand == "-" or operand == "/":
            again = 1
        else:
            print("pls try again")
    
    #gets the required value for the equation
    a = int(input("Enter A (T(n+1) = A(n) (operand) B): "))
    b = int(input("Enter B (T(n+1) = A(n) (operand) B): "))
    #gets the required value for the amount of tries used in the for loop
    tries = input("How many times do you want to try (type inf for infinite): ")
    accurate = int(input("how accurate do you want this to be (d.p.): "))
    #variables needed for the operation to function
    again = 0
    prevnum = n
    counter = 0
    answer = 0
    found = False
    #actual program
    while again == 0:
        #calculate t(n+1)
        if operand == "x" or operand == "*":
            answer = (a * n) * b
        elif operand == "/":
            answer = (a * n) / b 
        elif operand == "+":
            answer = (a * n) + b
        elif operand == "-":
            answer = (a * n) - b
        print(str(answer))
        #checks to see if previous number is the same as the current, if not previous number becomes current number
        if round(answer, accurate) == round(prevnum, accurate):
            found = True
            again = 1
        else:
            prevnum = answer
            n = answer

        #checks to see if user wanted to use infinite tries or a select number of tries and stops if it gets past a certain point
        if counter < 100000:
            if tries == "inf":
                counter == counter + 1
            else:
                if int(tries) == counter:
                    again = 1
                else:
                    counter = counter + 1
        else:
            again = 1
    #output
    if found == True:
        print("The final solution was found in " + str(counter) + " tries")
    else:
        print("The final solution was not found")

def average(inputstart):
    print("******AVERAGE******")
    mainagain = 0
    while mainagain == 0:
        numarray = []
        again = 0
        counter = 0 
        total = 0
        avg = 0
        while again == 0:
            print("******HINT****** \n If you want to stop just type 'x'")
            try:
                num = input(inputstart + "Enter the number you want to enter: ")
                if num == 'x':
                    again = 1
                else:
                    numarray.append(int(num))
                    counter = counter + 1
            except ValueError:
                print("Please enter an actual number")
            print(numarray)
            print(str(counter))
        for i in range(len(numarray)) :
            total = total + int(numarray[i - 1])
            print(total)
            avg = total / counter
        print(str(avg))
"""