n = int(input("Enter the amount of numbers: "))

for fizzbuzz in range(n):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("Fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("Fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("Buzz")
        continue
    print(fizzbuzz)
