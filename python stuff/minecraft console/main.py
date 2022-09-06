def version189():
    print("here")

def versionlatest():
    print("here 2")

def main():
    again = 1
    while again == 1:
        print("Text Adventures (Minecraft)")
        version = int(input("""******PICK VERSION******
        
        (Due to new blocks being added constantly 
        throughout minecraft's lifespan,
        you have to choose which version you want)
        
        Choose:
        1. 1.8.9 
        2. Latest
        3. Exit"""))

        if version == 1:
            version189()
        elif version == 2:
            versionlatest()
        else:
            again == 0

main()