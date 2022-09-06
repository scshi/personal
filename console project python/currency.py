import requests
import main as m

def currencies(currency, convertto):
    currencys = {

    }
    URL = "https://api.exchangerate-api.com/v4/latest/" + currency
    page = requests.get(URL)
    page = page.text.strip('}{')
    pages = page.split(',')
    print(pages)
    for i in range(len(pages)):
        whole = pages[i]
        print(whole)
        cur = whole[1] + whole[2] + whole[3]
        temp = whole[0] + cur + whole[4] + whole[5]
        whole = whole.strip(temp)
        currencys[cur] = whole
    return currency[convertto]

def convert(inputstart):
    currencyfrom = input(inputstart + "Enter the shorthand for the currency you want to convert from: ")
    howmuch = input(inputstart + "Enter the amount of the starting currency do you want to convert: ")
    cur = currencies(currencyfrom)


def rate(inputstart):
    currencyfrom = input(inputstart + "Enter the shorthand for the currency you want the conversion rate from")
    cur = currencies()

def choice(inputstart):
    print()
    menuchoice = int(input("""######MENU######
    1. convert from a selected currency
    2. see the conversion rate of one currency
    3+. Exit
    Enter here: """))
    if menuchoice == 1:
        convert(inputstart)
    elif menuchoice == 2:
        rate(inputstart)
    else:
        m.menumain()