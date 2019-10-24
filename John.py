from turtle import *

t = Turtle()
screen = t.getscreen()
t.forward(100)

def printname():
	name = screen.textinput("Shrek or nah", "name plz?")
	t.write(name, move=True, align="left", font=("Arial", 40, "normal"))
	screen.listen()

def forward():
	t.forward(50)

def right():
	t.right(90)

def left():
	t.left(90)

def back():
	t.backward(50)

def color():
	t.pencolor("red")

screen.onkey(color, "1")
screen.onkey(back, "s")
screen.onkey(left, "a")
screen.onkey(right, "d")
screen.onkey(forward, "w")
screen.onkey(printname, "p")

screen.listen()
screen.mainloop()


