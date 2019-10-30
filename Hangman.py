import time
import os

ASCII = ['''
    +----+
    |    |
         |
         |
         |
 =========''','''
    +----+
    |    |
    O    |
         |
         |
 =========''','''
    +----+
    |    |
    O    |
    |    |
         |
 =========''','''
    +----+
    |    |
   \O    |
    |    |
         |
 =========''',''' 
    +----+
    |    |
   \O/   |
    |    |
         |
 =========''','''
    +----+
    |    |
   \O/   |
    |    |
   /     |
 =========''','''
    +----+
    |    |
   \O/   |
    |    |
   / \   |
 ========='''      ]


print(ASCII[0])
word = "minecraft"
word = list(word)

print("Welcome to Hangman!")
guessList = []
missed = []
guessedLetters = []
for letter in word:
	guessList.append("_")
print(guessList)

while True:
	letter = input("Guess a letter: ")
	if letter == "m":
		guessList[0] = "m"
		print( )
		print("Thats a letter")
		guessedLetters.append(letter)
		print( )
		print("Guessed Letters" + str(guessedLetters))
		print(guessList)
	elif letter == "i":
		guessList[1] = "i"
		print("Thats a letter")
		print("Guessed Letters" + str(guessedLetters))
		print(guessList)
	elif letter == "n":
		guessList[2] = "n"
		print("Thats a letter")
		print("Guessed Letters" + str(guessedLetters))
		print(guessList)
	elif letter == "e":
		guessList[3] = "e"
		print("Thats a letter")
		guessedLetters.append(letter)
		print("Guessed Letters" + str(guessedLetters))
		print(guessList)
	elif letter == "c":
		guessList[4] = "c"
		print("Thats a letter")
		guessedLetters.append(letter)
		print("Guessed Letters" + str(guessedLetters))
		print(guessList)
	elif letter == "r":
		guessList[5] = "r"
		print("Thats a letter")
		guessedLetters.append(letter)
		print("Guessed Letters" + str(guessedLetters))
		print(guessList)
	elif letter == "a":
		guessList[6] = "a"
		print("Thats a letter")
		guessedLetters.append(letter)
		print("Guessed Letters" + str(guessedLetters))
		print(guessList)
	elif letter == "f":
		guessList[7] = "f"
		print("Thats a letter")
		guessedLetters.append(letter)
		print("Guessed Letters" + str(guessedLetters))
		print(guessList)
	elif letter == "t":
		guessList[8] = "t"
		print("Thats a letter")
		guessedLetters.append(letter)
		print("Guessed Letters" + str(guessedLetters))
		print(guessList)
	if guessList == word:
		print("You win")
		break
	
	else:
		print("That is not a letter, try again")
		missed.append(letter)
		print("These are the letters that you guessed so far" + str(guessedLetters))
		print(missed)
		print(ASCII[len(missed)])
		print(guessList)

