import turtle as t
from turtle import Turtle, Screen
import random

donnie = Turtle()
# donnie.shape('turtle')
donnie.color('purple')
t.colormode(255)
donnie.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)

    return color




# donnie.penup()
# donnie.sety(150)
# donnie.setx(50)
# donnie.pendown()


# Random Colors
# def generate_random_color():
#     hex_chars = "0123456789ABCDEF"
#     color = "#" + ''.join(random.choice(hex_chars) for _ in range(6))
#     return color
#
#
# colors = [generate_random_color() for _ in range(15)]




"""Challenge 1 (Draw a Square)"""

# for x in range(4):
#     donnie.fd(100)
#     donnie.lt(90)

"""Challenge 2 (Draw a dotted line)"""

# for _ in range(15):
#     donnie.fd(10)
#     donnie.penup()
#     donnie.fd(10)
#     donnie.pendown()

"""Challenge 3 (Draw different shapes)"""

# def draw(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         donnie.rt(angle)
#         donnie.fd(100)
#     donnie.pencolor(random.choice(colors))
#
#
# for shape_side_n in range(3, 11):
#     draw(shape_side_n)


"""Challenge 4 (Draw a random walk)"""

# directions = [0, 90, 180, 270]
# donnie.pensize(10)
# donnie.speed("fastest")
#
#
# def draw_random_walk():
#     donnie.color(random_color())
#     # Usas el setheading en reemplazo del right o left
#     donnie.setheading(random.choice(directions))
#     donnie.fd(30)
#
#
# for _ in range(200):
#     draw_random_walk()

"""Challenge 5 (Draw a Spirograph)"""


def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        donnie.circle(100)
        current_heading = donnie.heading()
        donnie.setheading(current_heading + size_of_gap)
        donnie.color(random_color())


draw_spirograph(50)




screen = Screen()
screen.exitonclick()
