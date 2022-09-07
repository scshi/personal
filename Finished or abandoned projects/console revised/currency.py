import requests
#4 subroutines
def conversionrate(currency, convertto):
    currencys = {
        "temp":0
    }
    URL = "https://api.exchangerate-api.com/v4/latest/" + currency
    page = requests.get(URL)
    page = page.text.strip('}')
    page = page.strip('{')
    pages = page.split(',')
    for i in range(len(pages)):
        whole = pages[i]
        cur = whole[1] + whole[2] + whole[3]
        temp = whole[0] + cur + whole[4] + whole[5]
        whole = whole.strip(temp)
        currencys[cur] = whole
    try:
        return currencys[convertto]
    except KeyError:
        return("NOT FOUND")

def convertrate(inputstart, currency):
    convertto = input(inputstart + " Enter the shorthand for the target currency: ")
    result = conversionrate(currency, convertto)
    print("1 " + currency + "is " + result + convertto)

def convertion(inputstart, currency):
    amount = int(input("Enter the amount of " + currency + ": "))
    convertto = input(inputstart + " Enter the shorthand for the currency you want to convert to: ").upper()
    convertrate = float(conversionrate(currency, convertto))
    if convertrate == "NOT FOUND":
        print(inputstart + "Not found")
    else:
        finalamount = int(convertrate * amount)
        print(str(amount) , currency + " is " + str(finalamount) , convertto)

def choice(inputstart):
    again = 1
    while again == 1:
        currency = input(inputstart + " Enter the shorthand for the base currency: ").upper()
        choose = int(input("""******MENU******
        1. See the conversion rate from starting currency
        2. Convert from one currency to another
        3+. Exit
        Enter here: """))
        if choose == 1:
            convertrate(inputstart, currency)
        elif choose == 2:
            convertion(inputstart, currency)
        else:
            again = 0