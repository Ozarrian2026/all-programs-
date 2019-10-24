# Calculations, printing, variables

# printing to the screen 
# The built in function print(), prints to the screen
# it will print both Strings and numbers
print("printing to the screen...")
print(" Bruh")# a string
print(" zombie bruh")
print(3) # a number
print("3") # a string
print(3 + 3 ) # 6
print("3" + "3") # string concatenation

# Performing Caculations\
# addition +
# subraction -
# multiplaction *
# division /
# exponents **
# modulo %

print(4 - 2) # subtraction 2
print( 4 * 2)# multiplaction 8
print(4 / 3) # division 1.333
print(4 ** 3)# exponents 64
print( "Modulo operator test")
print( 5 % 3)
print(10 % 2)
print(16 % 3)
# Modulo gives remainders
# python operators follow the same order of operations as Math
print(4 - 2 * 2)# should give zero
print((4 - 2) * 2)# should give 4

# Variables 
# variables are used to hold data 
# variable are declared and set to a value (initialzing)
badLuck = 13 # declared a variable called badLuck and initialized it to 13
# then can print the variable using it's name
print("badLuck = " + str(badLuck)) # cast it to a string 
# another variable 
goodLuck = "4" # string variable
print("goodLuck = " + goodLuck) # dont have to cast
badLuck + 5 # this pointless 
print(badLuck)
badLuck = badLuck + 5 # now bad luck is 18 
print(badLuck)

#can also save input into variables 
# using input() a prompt goes inside the ()
name = input("what is your name?")
print(" Hello" + name)
print (name * 10)
name = name + "\n" # escape character (new line)
print(name * 10)
# math 
base = input("Enter the base number:")
exp = input("Enter the exponent:")
print(int(base) ** int(exp)) 