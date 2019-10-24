print("Welcome to the To Do List")
# variable 
todo = []

while True:
	print(			)
	print("Enter a to add an item")
	print("Enter r for an item")
	print("Enter p to print out the list")
	print("Enter q to quit")
	print(			)
	
	choice = input("Choose one of the options given: ")

	if choice == "q":
		print("Goodbye, Have a nice day!")
		break
	elif choice == "a":
		a = input("What will be added to your to do list?: ")
		todo.append(a)
		print("Item added to your todo list")
	elif choice == "r":
		r = input("What would you like to remove from your list?: ")
		todo.remove(r)
		print("Removed from todo list")
	elif choice == "p":
		print("Printing todo list... " + str(todo))
	else:
		print("You choose something not given")