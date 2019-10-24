favFoods = ["rice", "brownies", "pizza"]
print(favFoods[0])
print(favFoods[2])
print(favFoods[1])
print(favFoods)
# adds to the end of the list
favFoods.append("cookies")
print(favFoods)
print("My 4th favorite food is " + favFoods[3])
# insert - Adds to an index in a list
favFoods.insert(1, "chicken")
print(favFoods)
# Remove item from the list
favFoods.remove("chicken")
print(favFoods)
# Remove an item using index
favFoods.pop(0)
print(favFoods)
favFoods.insert(0, "rice")
# Loop through a list
for food in favFoods:
	print(food)

numList = [3, 7, 9, 4, 1, 69, 74, 21]

# loop through the list and all the numbers together then print the sum

sum = 0
for num in numList:
	print(num)
	sum = sum + num

print("Total equals to: " + str(sum))
# Function to get the length of a list
print(len(numList))

# make a list of fav movies 
# prompt for a fav movie
favMovies = ["Zombie Land", "Nemo", "Up", "IT"]
movies = input("What is your favorite movie? ")
favMovies.append(movies)
print(favMovies)

# List method and functions
# append - adds an item to the end of a list
# insert - adds an item to a specified index
# remove - removes a specified item from list
# pop - removes an item from a specified index
# len - returns the length of a list
print(favFoods[len(favFoods)- 1])