import turtle
t = turtle.Turtle()
s = turtle.Screen()

def move_forward():
    t.forward(30)

def move_backward():
    t.backward(30)

def turn_left():
    t.left(30)

def turn_right():
    t.right(30)


def clear_screen():
    t.penup()
    t.clear()
    t.home()
    t.pendown()

s.listen()
s.onkey(move_forward, "w")
s.onkey(move_backward, "s")
s.onkey(turn_left, "a")
s.onkey(turn_right, "d")
s.onkey(clear_screen, "c")


s.mainloop()