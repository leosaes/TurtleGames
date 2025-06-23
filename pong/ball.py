from turtle import Turtle as t

class Ball(t):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color("white")
    self.penup()
    self.x = 1
    self.y = 1
    
  def move(self):
    x = self.xcor() + self.x
    y = self.ycor() + self.y
    self.goto(x,y)
    
  def bounce_y(self):
    self.y *= -1
  
  def bounce_x(self):
    self.x *= -1
  
  def reset(self):
    self.goto(0,0)
    self.bounce_x()