print ("Welcome to Currency Converter! \n  The commands are: \n  1. 'Convert' \n  2. 'Rates' \n  3. 'Quit'")
# Base currency is AUD - all other currencies calculated from this amount (rates from this amount)
rates_from = {'USD': 0.78, 'GBP': 0.55} #From Aussie $
rates_to = {'USD': 1.29, 'GBP': 1.83} #To Aussie $

def convert():
    amount = ''
    from_currency = ''
    to_currency = ''
    while not from_currency:
        from_currency = input("From (3 Letters eg AUD): ").upper()
    if from_currency == 'AUD':
        while not to_currency:
            to_currency = input("To (3 Letters eg GBP): ").upper()
        while not amount:
            amount = input("Enter Amount: ")
        amount = float(amount)
        for rate in rates_from:
            if rate == to_currency:
                focus_rate = rates_from[rate]
        result = amount * focus_rate
        result = result + 0.0001
        result = round(result, 4)
        result = str(result)
        print (result[:-2])
    else:
        while not to_currency:
            to_currency = input("To (3 Letters eg GBP): ").upper()
        if to_currency == "AUD":
            while not amount:
                amount = input("Enter Amount: ")
            amount = float(amount)
            for rate in rates_to:
                if rate == from_currency:
                    focus_rate = rates_to[rate]
            result = amount * focus_rate
            result = result + 0.0001
            result = round(result, 4)
            result = str(result)
            print (result[:-2])
        else:
            while not amount:
                amount = input("Enter Amount: ")
            amount = float(amount)
            for rate in rates_to:
                if rate == from_currency:
                    focus_rate = rates_to[rate]
            result = amount * focus_rate
            for rate in rates_from:
                if rate == to_currency:
                    focus_rate = rates_from[rate]
            result = result * focus_rate
            result = result + 0.0001
            result = round(result, 4)
            result = str(result)
            print (result[:-2])

def rates():
    print ("Rates: Aussie Dollars")
    for rate in rates_from:
        print (rate +':',rates_from[rate])
def menu():
    user = input("Enter Command: ").lower()
    while user:
        if "convert" in user:
            convert()

        elif "rates" in user:
            rates()

        elif "quit" in user:
            quit()
        else:
            print ("Command Not Recognised")
        user = input("Enter Command: ").lower()
menu()
