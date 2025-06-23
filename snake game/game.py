import turtle
import snake
import food
import time
import scoreboard

s = turtle.Screen()
t = snake.Snake()
f = food.Food()
sb = scoreboard.Score()

s.setup(600,600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)


s.listen()
s.onkey(t.up,"Up")
s.onkey(t.down,"Down")
s.onkey(t.left,"Left")
s.onkey(t.right,"Right")

game_on = True
while game_on:
    s.update()
    time.sleep(0.1)
    t.move()
    sb.create_scoreboard(sb.score)
    if t.head.distance(f) < 20:
      f.refresh()
      t.extend()
      t.speed_up()
      sb.create_scoreboard(sb.increase_score())

    if t.head.xcor() > 296 or t.head.xcor() < -296 or t.head.ycor() > 296 or t.head.ycor() < -296:
      sb.highscore()
      t.reset()

    for segment in t.segment[1:]:
       if t.head.distance(segment) < 15:
        sb.highscore()
        t.reset()

s.mainloop()
