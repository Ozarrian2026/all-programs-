
price = 0
given = 0
change = 0
dollars = 0
halfDollars = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0

price = float(input("How much was the price of the item?: "))
given = float(input("How much was given?: "))
change = given - price
print("Change Back is: " + str(change))
change = change * 100

dollars = int(change / 100)
change = change % 100

halfDollars = int(change / 50)
change = change % 50

