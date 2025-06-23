import turtle

FONT = ("Courier",24,"normal")

class Scoreboard(turtle.Turtle):
  def __init__(self):
    super().__init__()
    self.level = 1
    self.create_score(self.level)
    
  def create_score(self, level):
    self.hideturtle()
    self.clear()
    self.penup()
    self.color("black")
    self.goto(-100,250)
    self.write(f"Level {level}",align="center", font=FONT)
  
  def increase(self):
    self.level+=1
    self.create_score(self.level)