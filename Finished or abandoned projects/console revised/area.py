import math

def triangle(inputstart):
    print(inputstart + "******AREA - TRIANGLE******")
    again = 0
    while again == 0:
        try:
            height = int(input("Enter the height of the triangle: "))
            width = int(input("Enter the width of the triangle: "))
            area = (height * width) / 2
            print(inputstart , str(area) + " is the area of the triangle: " + str(width) + "cm X " + str(height) + "cm")
        except ValueError:
            print("Pls enter a number")

def rectangle(inputstart):
    print(inputstart + "******AREA - RECTANGLE******")
    again = 0
    while again == 0:
        try:
            height = int(input("Enter the length of the rectangle: "))
            width = int(input("Enter the width of the rectangle: "))
            area = height * width
            print(inputstart , str(area) + " is the area of the rectangle: " + str(width) + "cm X " + str(height) + "cm")
        except ValueError:
            print("Pls enter a number")

def vcuboid(inputstart):
    print(inputstart + "******VOLUME******")
    again = 0
    while again == 0:
        try:
            length = int(input("Enter the Length (cm): "))
            height = int(input("Enter the Height (cm): "))
            width = int(input("Enter the Width (cm): "))
            volume = length*height*width
            print(inputstart , str(volume) + " is the volume of the cuboid: " + str(length) + "cm X " + str(height) + "cm X " + str(width) + "cm")
        except ValueError:
            print("Pls enter a number")

def sphere(inputstart):
    print(inputstart + "******VOLUME******")
    again = 0
    while again == 0:
        try:
            radius = int(input("Enter the Radius (cm): "))
            volume = 4 * (radius^2 * math.pi())
            print(inputstart + str(volume) + " is the volume of the " + str(radius) + " cm sphere")
        except ValueError:
            print("Pls enter a number")
            