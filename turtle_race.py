from turtle import Turtle, Screen
import random

#  just make a bet on a color nd its not rigged !

s = Screen()
s.setup(width = 500, height =  400)
choice = s.textinput("Bet", "Bet who wins (red, green, black, blue): ")


d1 = 0
d2 = 0
d3 = 0
d4 = 0
win = ""


t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t1.shape("turtle")
t2.shape("turtle")
t3.shape("turtle")
t4.shape("turtle")


t1.color("red")
t2.color("black")
t3.color("green")
t4.color("blue")


t1.up()
t2.up()
t3.up()
t4.up()


t1.goto(-230,100)
t2.goto(-230,50)
t3.goto(-230,-50)
t4.goto(-230,-100)


while True:
   r1 = random.randint(10,40)
   r2 = random.randint(10,40)
   r3 = random.randint(10,40)
   r4 = random.randint(10,40)

   d1 += r1
   d2 += r2
   d3 += r3
   d4 += r4

   t1.forward(r1)
   t2.forward(r2)
   t3.forward(r3)
   t4.forward(r4)

   if d1 >= 460 or d2 >= 460 or d3 >= 460 or d4 >= 460 :
      break


if d1 >= 460:
   win = "red"
elif d2>= 460:
   win = "black"
elif d4>= 460:
   win = "blue"
elif d3>= 460:
   win = "green"


if choice == win:
   print("You win")
else:
   print("You lose")


s.exitonclick()
