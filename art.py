import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle
artist = turtle.Turtle()
artist.speed(0)
artist.width(2)
artist.hideturtle()

# Number of colors and hue step
n = 36
hue = 0

# Artistic pattern
for i in range(360):
    # Set the color using HSV to RGB conversion for rainbow effect
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    artist.pencolor(color)
    artist.forward(i * 3 / n + i)
    artist.left(59)
    artist.forward(i * 3 / n + i)
    artist.left(59)
    artist.forward(i * 3 / n + i)
    artist.left(59)

    hue += 0.005  # Slightly shift the hue

# Exit on click
screen.exitonclick()
