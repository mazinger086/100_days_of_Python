import random
import turtle
import turtle as turtle_module
from random import choice

turtle_module.colormode(255)
turtle.title("Hirst Painting")

color_list = [(1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39),
              (215, 87, 64), (164, 162, 32), (158, 6, 24), (157, 62, 102), (11, 63, 32), (97, 6, 19),
              (207, 74, 104), (10, 97, 58), (0, 63, 145), (173, 135, 162), (7, 172, 216), (158, 34, 24),
              (3, 213, 207), (8, 140, 85), (145, 227, 216), (122, 193, 148), (102, 220, 229), (221, 178, 216),
              (253, 197, 0), (80, 135, 179)]

tim = turtle_module.Turtle()
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 101
tim.speed("fastest")

for dot in range(1, number_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.fd(50)

    if dot % 10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)








screen = turtle_module.Screen()
screen.exitonclick()

