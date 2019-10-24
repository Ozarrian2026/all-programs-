from turtle import *
st = Turtle()
t = Turtle()
myScreen = st.getscreen()
st.penup()
st.goto(myScreen.window_width() / 2 - 200, myScreen.window_height()/ 2 - 50)
st.hideturtle()
score = 0
screen = t.getscreen

def updateScore():
  st.clear()
  st.write("Score:" + str(score), False,"left", font=("Times New Roman", 20, "normal"))

updateScore()

myScreen.mainloop() 
