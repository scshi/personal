centigrade  = int(input("Enter the temperature in centigrade: "))
while centigrade > 100 and centigrade < 0:
    print("Temperature must be between 0 and 100")
    centigrade = int(input("Enter the temperature in centigrade: "))
fahrenheit = centigrade * (9 / 5) + 32
print(str(fahrenheit))
