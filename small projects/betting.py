#A user can bet on any number from 0 to 30. If it’s an even number they 2x their money back. If it’s a multiple of 10 they get 3x their money back. If it’s a prime number they
#get 5x their money back. If the number is below 5 they get a 2x bonus.
#Create a program that allows the user to guess a number. A random number is generated. If the guess == the random number then the user wins and gets a pay-out.
#Combinations of the win scenarios should be catered for.. e.g. 20 wins 2 x 3 bonus = 6x their money.
import random
money = 0

again = 'y'
while again == 'y':
    betnum = random.randint(0,30)
    betting = int(input("Bet your number"))
    num = False
    if betnum > 1:
        for i in range(2, num//2):
            if (num % i) == 0:
                break
            else:
                num = True
    if betting == betnum:
        if betting%2 == 0:
            money = money + (betting*2)
        elif betting%10 == 0:
            money = money + (betting*3)
        elif num == True:
            money = money + (betting*5)
        elif num <= 5:
            money = money + (betting*2)
        else:
            money = money + betting
