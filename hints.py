
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