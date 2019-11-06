import time
import os

# variables
hours = 0
minutes = 0
seconds = 0

# input
print("Enter the number of hours, minutes, and seconds for the timer")
hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))

#covert seconds
minutes += hours * 60
seconds += minutes * 60


# set hours and minutes to zero
minutes = 0
hours = 0

# start the countdown loop
while seconds >= 0:
	# convert back to hours, minutes, seconds to print time 
	minutes = int(seconds / 60)
	seconds = seconds % 60

	hours = int(minutes / 60)
	minutes = minutes % 60

	# print time 
	print(str(hours) + ":" + str(minutes) + ":" + str(seconds))

	# convert back to seconds
	minutes += hours * 60
	seconds += minutes * 60


	# set hours and minutes to zero
	minutes = 0
	hours = 0
	# pause for a second
	time.sleep(1)
	# clear the scereen 
	os.system("cls")
	# subtract a second, loop back
	seconds -= 1