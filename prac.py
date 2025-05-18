import turtle as t
#to understand class and objects OOPs
ok = t.Turtle()
ok.shape("turtle")
ok.color("black", "green")


ok.forward(100)
ok.left(90)
ok.backward(100)
ok.left(90)
ok.forward(120)
ok.left(90)
ok.backward(120)
ok.left(90)
ok.forward(140)
ok.left(90)
ok.backward(140)
ok.left(90)
ok.forward(160)
ok.left(90)
ok.backward(160)
ok.left(90)
ok.forward(180)
ok.left(90)
ok.backward(180)
ok.circle(10)
ok.clear()


my_screen = t.Screen()
my_screen.canvheight()
my_screen.exitonclick()

print(ok)
