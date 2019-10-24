HI = input("Hello what is your name? ")
print("Hello " + HI)

No = input("Would you like to play a game? ")
if No == "no":
	print("Alright, see you later then.")

if No == "yes":
	print("Then let's get started!")
	num = 3
	guess = input("Choose a number between 1 and 15:")
	guess = int(guess)
	if guess == num:
		print("Nice, you guessed it")
	elif guess > num:
		print("Too High m8")
	else:
		print("Too Low bro")
		print("Try again later")
	print("Thanks for playing!")

