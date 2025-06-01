from turtle import Turtle, Screen

#  read the onkey functions at the bottom to learn bout movements n functioning

t = Turtle()
s = Screen()

def moveForward():
   t.forward(12)

def moveBack():
   t.backward(12)

def turnLeft():
   t.left(15)

def turnRight():
   t.right(15)

def clrscr():
   s.clearscreen()

def right90():
   t.right(90)

def left90():
   t.left(90)

def Up():
   t.up()

def Down():
   t.down()
   



s.listen()
s.onkey(key="w", fun=moveForward)
s.onkey(key="s", fun=moveBack)
s.onkey(key="c", fun=clrscr)
s.onkey(key="a", fun=turnLeft)
s.onkey(key="d", fun=turnRight)
s.onkey(key="r", fun=right90)
s.onkey(key="r", fun=left90)
s.onkey(key="u", fun=Up)
s.onkey(key="o", fun=Down)
s.exitonclick()