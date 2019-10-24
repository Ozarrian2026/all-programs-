# Ozarrian John
# Block 1
# Dice Rolling Simulator

import random

numRolls = int(input("Enter the amount of rolls: "))

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
rollNum = 1
while rollNum <= numRolls:
	print("Total Rolls: " + str(numRolls))
	randomNum = random.randint(1, 6) 
	if randomNum == 1:
		print("Roll number: " + str(randomNum))
		one = one + 1
		
	if randomNum == 2:
		print("Roll number: " + str(randomNum))
		two = two + 1
		
	if randomNum == 3:
		print("Roll number: " + str(randomNum))
		three = three + 1
		
	if randomNum == 4:
		print("Roll number: " + str(randomNum))
		four = four + 1
		
	if randomNum == 5:
		print("Roll number: " + str(randomNum))
		five = five + 1
		
	if randomNum == 6:
		print("Roll number: " + str(randomNum))
		six = six + 1
	break
print("1s: " + str(one))
print("2s: " + str(two))
print("3s: " + str(three))
print("4s: " + str(four))
print("5s: " + str(five))
print("6s: " + str(six))