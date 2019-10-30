
# Hints!
myWord = "hello"
choice = input("Type a word: ")
if choice == myWord:
	print("Its a match")
else:
	print("Not a match")

letter = input("Enter a letter: ")

if letter in myWord:
	print("Letter is in word")
else:
	print("Letter is not in word")

count = 0

myList = list(myWord)
for letter2 in myList:
	if letter2 == letter:
		print(count)
	count += 1

myString = "Arizona"
mysteryWord = list(myString)
print(mysteryWord)
guessList = []
#prints word with letters seperated
for letter in mysteryWord:
	guessList.append("_")
print(guessList)
# how to replace a specfic index in a list
guessList[3] = "z"

print(guessList)

# timer for hangman
#boom = 10
#while boom > 0:
	#time.sleep(0)
	#print(boom)
	#boom -= 1
#print("Times Up!")


secertWord = "christmas"
secertWord = list(secertWord)
print(secertWord)
misses = 0
hangman = ["first pic", "second pic"]

guess = input("Guess a letter: ")

if guess in secertWord:
	print("letter in a word")
else:
	misses = misses + 1

print("Misses: " + str(misses))
print(hangman[misses])

# how to replace the under score's with letters

mystery = "halloween"
mystery = list(mystery)

myGuess = "_________"
myGuess = list(myGuess)

guess1 = input("Guess a letter: ")

if guess1 in mystery:
	count = 0
	for letter in mystery:
		if letter == guess1:
			myGuess[count] = guess1
		count += 1

print(myGuess)












# hints for FizzBuzz
myNum = int(input("Enter a number to check: "))

print("Checking if your number is a multiple of 3")

# % gives remainders
# Check if the remainder is zero

if myNum % 3 == 0:
	print("your number is a multiple of 3")

# Check if number is a multiple of 5

if myNum % 5 == 0:
	print("your number is a multiple of 5")

# How to print on the same line
print(str(myNum), end="")
print(" something else")