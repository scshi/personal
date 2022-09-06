# Create a phone extension manager
# The manager should allow you to do the following:
    # View exisiting contacts and extensions
    # Add a new contact and extension
    # Edit an existing contact
    # Delete a contact and extension
    # View contacts by first initial
    # View contacts by second initial

def menu():
    choice = int(input("""******Phone list manager******
    1. View exisiting contacts and extensions
    2. Add a new contact and extension
    3. Edit an existing contact
    4. Delete a contact and extension
    5. View contacts by first initial
    6. View contacts by second initial"""))
    return choice

def print_all(phone_list):
    for x, y in phone_list.items():
        print(x, y)
    return 0

def new_contact(phone_list):
    x = input("******INPUT****** \n Please input a name: ")
    y  = int(input("******INPUT****** \n Please input a number: "))
    phonelist.update(x, y)
    return 0

def edit_contact(phone_list):
    userinput = input("******INPUT****** \n Please input the name or number \n you would like to change: ")
    for x,y in phone_list.items():
        if userinput == x or y:
            changeinput = input("******INPUT****** \n Please input the new \n name or number: ")
        else:
            print("******ERROR****** \n Sorry, value not found...")
    pass

def delete_contact(phone_list):
    pass

def view_by_first_initial(phone_list):
    pass

def view_by_second_initial(phone_list):
    pass


phone_list = {"K.Clown": 121,"K.Vanhouten":333,"K.Brockman":233,"B.Gumble":444,"M.Syzlak":185} #for the phone list manager
menuchoice = int(input("""These are the project over yr 10 and yr 11:
    1) phonelist manager
    2) card drawer deck thing
    3) exit"""))

if menuchoice == 1:
    choice = menu()
    while choice != 7:
        if choice == 1:
            print_all(phone_list)
        elif choice == 2:
            phone_list = new_contact(phone_list)
        elif choice == 3:
            phone_list = edit_contact(phone_list)
        elif choice == 4:
            phone_list = delete_contact(phone_list)
        elif choice == 5:
            view_by_first_initial(phone_list)
        elif choice == 6:
            view_by_second_initial(phone_list)
        choice = menu()
    input("Thank you for using the Extension Manager program. Press enter to close.")
