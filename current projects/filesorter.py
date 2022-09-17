#needed to explore C:\ drive
import os 
import shutil 

#main base of the program
def fileexplorer():
    choice = int(input("""******CHOICE******
1. Only see folders
2. See everything"""))

    path = ("C:\\Users")
    path_part = []

    again = 1
    while again == 1:

        list_ = os.listdir(path)
        
        print(" - " + str(path))

        #printing the amount of folders and/or files
        if choice == 1:

            #only folders
            amtfolder = onlyfolders(path, list_)
            print("Amount of folders: " + str(amtfolder))
        else:

            #both files and folders
            amtfolder, amtfile = allfolders(path, list_)
            print("Amount of files: " + str(amtfile))
            print("Amount of folders: " + str(amtfolder))

        #asks for next part of path and applies it
        pathnew = path + "\\" + input("Enter the folder/file you want to open: ")
        if os.path.isdir(pathnew):
            list_ = os.listdir(pathnew)
            allfolders(pathnew, list_)
        else: 
            pathnew = path + "\\" + input("Enter the folder/file you want to open: ")
            



def onlyfolders(path, list_):
    amtfolder = 0
    for i in range(len(list_)):
        if os.path.isdir(path + "\\" + list_[i]):
            print("\033[1;33;40m | (Folder) - " + list_[i])
            amtfolder = amtfolder + 1
    return amtfolder

def allfolders(path, list_):
    amtfolder = 0
    amtfile = 0
    folder = []
    file = []
    for i in range(len(list_)):
            if os.path.isdir(path + "\\" + list_[i]):
                folder = folder.append(list_[i])
                amtfolder = amtfolder + 1
            else:
                print("\033[1;30;40m | (File)   - " + list_[i])
                amtfile = amtfile + 1
    return amtfolder, amtfile
    
fileexplorer()    