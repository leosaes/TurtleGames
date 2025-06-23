import turtle
from random import choice, randint
s = turtle.Screen()
s.setup(500,400)

colors = ["red", "blue", "green", "yellow", "purple", "orange"]

is_race_on = False

bet = s.textinput("Bet!","What turtle do you think will win?").lower()

speeds = [10, 8, 7, 5, 3, 2]

def create_turtle():
    return turtle.Turtle(shape="turtle")


turtles = []
for i in range(6):
  t = create_turtle()
  t.color(colors[i])
  t.penup()
  t.goto(-240,-120+50*i)
  turtles.append(t)


if bet:
   is_race_on = True

while is_race_on: 

    for t in turtles:
      if t.xcor() > 217:
        win = t.pencolor()
        if bet == win:
          print("Winner!", f"You've won! The {win} turtle is the winner!")
        else:
          print("Loser!", f"You've lost! The {win} turtle is the winner!")
        is_race_on = False
      t.speed(choice(speeds))
      t.forward(randint(0,10))
        


s.mainloop()