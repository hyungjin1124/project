import colorgram
import turtle as t
import random

# Use a wide range of rgb.
t.colormode(255)
tim = t.Turtle()
tim.hideturtle()
tim.speed(10)
 
# Extract 30 color from image using colorgram. And make color list.
colors = colorgram.extract('./image/color_spot.jpg', 30)
colors_list = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

tim.penup()
starting_pos_x = -200
starting_pos_y = -200

for _ in range(10):
    tim.setpos(starting_pos_x, starting_pos_y)
    starting_pos_y += 50
    for _ in range(10):
        tim.dot(20, random.choice(colors_list))
        tim.forward(50)

screen = t.Screen()
screen.exitonclick()