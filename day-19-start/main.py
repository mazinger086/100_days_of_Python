from turtle import Turtle, Screen
import random

colors = ["red", "blue", "purple", "orange", "black", "yellow"]

is_race_on = False
screen = Screen()
screen.setup(width=520, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter color")

y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
race_list = []


def draw_goal():
    goal = Turtle()
    goal.hideturtle()
    goal.penup()
    goal.goto(220, -140)
    goal.setheading(90)
    goal.pendown()
    goal.pensize(5)
    goal.fd(280)


def draw_table():
    print("*------------------------------*")


draw_goal()

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-220, y=y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    contador = 0

    for index, turtle in enumerate(all_turtles):
        contador += 1
        print({turtle.xcor(): turtle.pencolor()})

        if contador >= len(all_turtles):
            contador = 0
            print("\n")

        if turtle.xcor() > 220:
            winning_color = turtle.pencolor()



            is_race_on = False
            if winning_color == user_bet:
                print(f"Congratulation you Won!! The winning turtle was: {winning_color}")
            else:
                print(f"Sorry you lose the race against {winning_color} turtle")

        random_distance = random.randint(0, 10)
        turtle.fd(random_distance)


screen.exitonclick()
