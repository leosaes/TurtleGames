from turtle import Turtle
from random import choice, randint

COLORS = ["red","orange","yellow","blue","purple","black"]
STARTING_MOVE = 5
MOVE_INCREMENT = 10

class Car(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("square")    
    self.shapesize(stretch_len=2)
    self.penup()
    self.color(choice(COLORS))
    self.goto(310,randint(-240,240))  
  
  def move(self):
    self.setheading(180)
    self.forward(STARTING_MOVE)
    

     