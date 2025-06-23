from turtle import Turtle as t

class Score(t):
  def __init__(self):
    super().__init__()
    self.score_p1 = 0
    self.score_p2 = 0
    self.clear()
    self.penup()
    self.hideturtle()
    self.color("white")
    self.create_scoreboard()

  def create_scoreboard(self):
    self.clear()
    self.goto(-100,200)
    self.write(f"{self.score_p1}", align="center", font=("Courier", 50, "normal"))
    self.goto(100,200)
    self.write(f"{self.score_p2}", align="center", font=("Courier", 50, "normal"))
  
  def increase_score_p1(self):
    self.score_p1 += 1
    self.create_scoreboard()

  def increase_score_p2(self):
    self.score_p2 += 1
    self.create_scoreboard()