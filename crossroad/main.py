import turtle as t
import time
import player
import car
import scoreboard

s = t.Screen()
sb = scoreboard.Scoreboard()
p = player.Player()

s.setup(600,600)
s.title("Crossroad")
s.tracer(0)

s.listen()
s.onkeypress(p.move,"Up")

time_s = 0.1
new_car = []
count = 0
game_on = True
while game_on:
  time.sleep(time_s)
  s.update()  

  for cars in new_car:
    cars.move()

    if p.distance(cars) < 30:
      print("loser")
      game_on = False

  if count % 6 == 0:
    new_car.append(car.Car())

  if p.ycor() > 280:
    p.reset()
    sb.increase()
    time_s*=0.9
    
  count+=1

s.mainloop()