import turtle as t
import paddle
import ball
import scoreboard
import time

s = t.Screen()
s.title("Pong Game")
s.setup(width=800, height=600)
s.bgcolor("black")
s.tracer(0) 

p1 = paddle.Paddle(-380,0)
p2 = paddle.Paddle(380,0)
b = ball.Ball()
sb = scoreboard.Score()

line = t
line.penup()
line.goto(0,300)
line.setheading(270)
line.color("white")
line.shapesize(stretch_wid=1)

for _ in range(10):
  line.pendown()
  line.forward(30)
  line.up()
  line.forward(30)

s.listen()
s.onkeypress(p1.move_up, "w")
s.onkeypress(p1.move_down, "s")
s.onkeypress(p2.move_up, "Up")
s.onkeypress(p2.move_down, "Down")

is_true = True
time_s = 0.01
while is_true:
  time.sleep(time_s)
  s.update()
  b.move()

  if b.ycor() > 290 or b.ycor() < -290:
    b.bounce_y()

  if b.distance(p2) < 50 and b.xcor() >360 or b.distance(p1) < 50 and b.xcor() < -360:
    time_s *=0.8
    b.bounce_x()
    

  if b.xcor() > 390:
    sb.increase_score_p1()
    b.reset()
    time_s=0.01
    

  if b.xcor() < -390:
    sb.increase_score_p2()
    b.reset()
    time_s=0.01
    

s.mainloop()