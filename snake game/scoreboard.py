from turtle import Turtle 

with open("data.txt",mode="r") as data:
  hs = data.read()

class Score(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.high_score = int(hs)
    self.create_scoreboard(self.score)
    
  def create_scoreboard(self, score):
    self.clear()
    self.penup()
    self.hideturtle()
    self.color("white")
    self.goto(0, 260)
    self.write(f"Score: {score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

  def increase_score(self):
    self.score += 1
    return self.score
  
  def highscore(self):
    if self.score > self.high_score:
      self.high_score = self.score
      with open("data.txt",mode="w") as data:
        data.write(str(self.high_score))
    self.score = 0
    self.create_scoreboard(self.score)
  
 # def game_over(self):
 #   self.goto(0, 0)
 #   self.color("red")
 #   self.write("Game Over", align="center", font=("Arial", 24, "normal"))