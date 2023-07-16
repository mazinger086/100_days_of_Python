# import colorgram
#
# colors = colorgram.extract('dots.jpg', 30)
#
# rgb_colors = []
#
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)
#
# print(rgb_colors)
import turtle
from turtle import Turtle, Screen
from random import choice

turtle.colormode(255)

color_list = [(1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39),
              (215, 87, 64), (164, 162, 32), (158, 6, 24), (157, 62, 102), (11, 63, 32), (97, 6, 19),
              (207, 74, 104), (10, 97, 58), (0, 63, 145), (173, 135, 162), (7, 172, 216), (158, 34, 24),
              (3, 213, 207), (8, 140, 85), (145, 227, 216), (122, 193, 148), (102, 220, 229), (221, 178, 216),
              (253, 197, 0), (80, 135, 179)]

mike = Turtle()
mike.penup()
mike.ht()
mike.sety(-250)
mike.setx(-300)
mike.st()
mike.speed(0) #"fastest"

screen = Screen()
w_screen = screen.window_width() // 2


def paint_dots():
    for dot in range(10):
        mike.fd(25)
        mike.dot(20, choice(color_list))
        mike.fd(25)


def turn_up():
    mike.lt(90)
    mike.fd(50)
    mike.rt(90)
    mike.setx(-300)


for _ in range(10):
    paint_dots()
    turn_up()

mike.ht()
screen.exitonclick()
