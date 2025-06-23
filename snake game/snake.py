import turtle

INICIAL_POSITIONS = [(0,0), (-20,0), (-40,0)]
DISTANCE = 20

class Snake:
  def __init__(self):
    self.segment = []
    self.create_snake()
    self.head = self.segment[0]
    self.speed = 0.1
    
  def create_snake(self):
    for position in INICIAL_POSITIONS:
      self.add_segment(position)

  def reset(self):
    for seg in self.segment:
      seg.goto(1000,1000)
    self.segment.clear()
    self.create_snake()
    self.head = self.segment[0]

  def add_segment(self, position):
    t = turtle.Turtle(shape="square")
    t.color("white")
    t.penup()
    t.goto(position)
    self.segment.append(t)
    
  def extend(self):
    self.add_segment(self.segment[-1].position())

  def move(self):
      for num in range(len(self.segment)-1,0,-1):
        self.segment[num].goto(self.segment[num-1].xcor(), self.segment[num-1].ycor())
      self.head.forward(DISTANCE)  

  def up(self):
    if self.head.heading() != 270:
      self.head.setheading(90) 
         
  def down(self):
    if self.head.heading() != 90:
      self.head.setheading(270) 
  
  def left(self):
    if self.head.heading() != 0:
      self.head.setheading(180) 
  
  def right(self):
    if self.head.heading() != 180:
      self.head.setheading(0) 

  def speed_up(self):
    self.speed +=0.1
    if self.speed == 10:
      self.speed -=0.1
    


    