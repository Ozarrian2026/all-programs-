import time
import os

frameList = ['''
  +---+
  o   |
 /|\  |
 / \  |
     === 
 ''',
 '''
  +---+   
  \\o/ |
   |  |
   \\\ |
     ===''']

while True:
	os.system("cls")
	for frame in frameList:
		print(frame)
		time.sleep(.2)
		os.system("cls")

print(frameList[0])

animation = ['''
  XD''',
  '''

  ;P ]