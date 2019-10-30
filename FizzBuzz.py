# print all intergers to 100
# cannot use 100 prints
# use a loop


for x in range(100):
	x = 0
while True:
	if x < 100:
		x = x + 1
		if x % 3 == 0 and x % 5 == 0:
			print(str(x), end= "")
			print(" Fizz Buzz")
		elif x % 3 == 0:
			print(str(x), end= "")
			print(" Fizz")
		elif x % 5 == 0:
			print(str(x), end= "")
			print(" Buzz")
		else:
			print(x)