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
for letter in word:
	guessList.append("_")
print(guessList)

while True:
	guess = input("Guess a letter: ")
	if guess == "m":
		guessList[0] = "m"
		print(guessList)
		print("There is that letter in this word")
	elif guess == "i":
		guessList[1] = "i"
		print(guessList)
		print("There is that letter in this word")
		print(ASCII)
	elif guess == "n":
		guessList[2] = "n"
		print(guessList)
		print("There is that letter in this word")
		print(ASCII)
	elif guess == "e":
		guessList[3] = "e"
		print(guessList)
		print("There is that letter in this word")
		print(ASCII)
	elif guess == "c":
		guessList[4] = "c"
		print(guessList)
		print("There is that letter in this word")
		print(ASCII)
	elif guess == "r":
		guessList[5] = "r"
		print(guessList)
		print("There is that letter in this word")
		print(ASCII)
	elif guess == "a":
		guessList[6] = "a"
		print(guessList)
		print("There is that letter in this word")
		
	elif guess == "f":
		guessList[7] = "f"
		print(guessList)
		print("There is that letter in this word")
		
	elif guess == "t":
		guessList[8] = "t"
		print(guessList)
		print("There is that letter in this word")
		
	else:
		print(ASCII[1])
		print("That is not a letter in the word")
		print("Try again")
		print(guessList)



print(ASCII)