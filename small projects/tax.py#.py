def tax():
    sal = int(input("Enter your salary per year: "))
    if sal <= 12570:
        print("Your final salary is £" + str(sal))
    elif sal > 150000:
        tax = sal * 0.55
        print("Your final salary is £" + str(tax))
    elif sal > 50271:
        tax = sal * 0.60
        print("Your final salary is £" + str(tax))
    else:
        tax = sal * 0.8
        print("Your final salary is £" + str(tax))

tax()
