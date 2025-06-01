import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle
artist = turtle.Turtle()
artist.speed(0)
artist.width(2)
<<<<<<< HEAD
artist.shape("triangle")
# artist.hideturtle()
=======
# artist.hideturtle()
artist.shape("triangle')
>>>>>>> fbb753170b894bf2c5d18a5d18bdafabdce1fb83

# Number of colors and hue step
n = 36
hue = 0

for i in range(360):
    
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    artist.pencolor(color)
    artist.forward(i * 3 / n + i)
    artist.left(59)
    artist.forward(i * 3 / n + i)
    artist.left(59)
    artist.forward(i * 3 / n + i)
    artist.left(59)

    hue += 0.005  # Slightly shift the hue

screen.exitonclick()
