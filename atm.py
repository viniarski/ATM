
# user data
customers = {
    1111 : {'pin' : 1234, 'balance' : 500.0},
    2222 : {'pin' : 2345, 'balance' : 1500.0},
    3333 : {'pin' : 3456, 'balance' : 1000.0},
    4444 : {'pin' : 4567, 'balance' : 250.0},
    5555 : {'pin' : 5678, 'balance' : 10000},
    }

# checks if card is in the database
card = int(input("What is your card number: "))

while card not in customers:
    print("Card doesn't match database. Please try again.")
    card = int(input("What is your card number: "))

# main loop
active = True
while active:
    pin_check = 2
    pin = int(input("PIN: "))
# checks if PIN matches the card number
    if pin != customers[card]['pin'] and pin_check != 0:
        print("PIN doesn't match. Please try again.")
        pin_check -= 1
    elif pin != customers[card]['pin'] and pin_check == 0:
        print("\nToo many attempts.\nYour card has been blocked.")
        active = False
    else:
# gives the prompt to choose an option
        prompt = "\nPlease enter an option:"
        prompt += "\n\t1. Balance"
        prompt += "\n\t2. Cash"
        prompt += "\n\t3. Quit. "
        prompt += "\n\tEnter: "

        choose = int(input(prompt))

        if choose == 1:
            print("Checking balance...")
            print("Your balance is: $", customers[card]['balance'])
        elif choose == 2:
            print("Whitdrawing money...")
            active = False # change this line
        elif choose == 3:
            active = False