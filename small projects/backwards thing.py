def my_function(x):
  return x[::-1]

again = 'y'

while again == 'y':
    mytxt = input("Enter the text: ")
    mytxt2 = my_function(mytxt)

    if mytxt == mytxt2:
        print("You put in the palindrome: " + mytxt)
    else:
        print(mytxt2)

    again = input("Do you to go again? ")
    if again == 'Y' or again == "Yes" or again == 'y':
        again = 'y'
    else:
        again = 'n'

