from turtle import Turtle as t

class Paddle(t):
  def __init__(self,x,y):
    super().__init__()
    self.shape("square")
    self.color("white")
    self.penup()
    self.speed("fastest")
    self.position = self.goto(x,y)
    self.shapesize(stretch_wid=5,stretch_len=1)
  
  def move_up(self):
    self.setheading(90)
    self.shapesize(stretch_wid=1,stretch_len=5)
    self.forward(10)
  
  def move_down(self):
    self.setheading(270)
    self.shapesize(stretch_wid=1,stretch_len=5)
    self.forward(10)