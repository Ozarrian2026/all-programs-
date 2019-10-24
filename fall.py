# This is a check/review to make sure nothing was "lost" over break

# Ozarrian John
# B-1

#Variable declaration and assignment
# ex
myVar = "hello"
# you try, declare two variables 1 string and 1 number, and assign values
age = 14
myName = "Ozarrian"
# while loop
# Example
x = 10
while x > 0:
	print(x)
	x = x - 1
# you try, print name 100 times
y = 100
while y > 0:
	print(myName)
	y = y - 1
# string concatenation
# Example
name = "Ozarrian"
print("Hello " + name)
# make a varaible with your favorite movie
# print "My favorite movie is " and then the value stored in the variable
movie = "Zombie Land"
print("My favorite movie is " + movie)

# input
# Ex
myname = input("What is your name: ")
print("Your name is: " + myname)
# prompt for favorite song and print "Ypur favorite song is: "
song = input("What is your favorite song: ")
print("Your favorite song is: " + song)

# casting: changing the type of a variable
myNumber = 40
print("My number is " + str(myNumber))
num1 = input("Enter a number: ")
num1 = int(num1) + 10
print("num1 + 10 is " + str(num1))

# ask for 2 numbers, add them and print
Num1 = input("Enter first number: ")
Num2 = input("Enter second number: ")
print("Total is:")
print(int(Num1) + int(Num2))

# if/else
# ex
num = int(input("Type a number: "))
if num > 100:
	print("Your number is more than 100")
elif num == 100:
	print("Your number is equal to 100")
else:

	print("Your number is less than 100")

# ask if today is your birthday, if it is than print happy birthday
birthday = input("Is it your birthday today? ")
if birthday == "yes":
	print("Happy Birthday")
elif birthady == "no":
	print("Okay then have a good day")