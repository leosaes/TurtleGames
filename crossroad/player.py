import turtle

STARTING_POS = (0,-280)
MOVING = 10
FINISH = 280

class Player(turtle.Turtle):
  def __init__(self):
    super().__init__()
    self.shape("turtle")
    self.color("green")
    self.penup()
    self.goto(STARTING_POS)
    self.move()
  
  def move(self):
    self.setheading(90)
    self.forward(MOVING)
  
  def reset(self):
    if self.ycor() > FINISH:
      self.goto(STARTING_POS)