from turtle import Turtle, Screen

donnie = Turtle()
donnie.speed(0)
screen = Screen()


def move_forwards():
    donnie.fd(10)


def move_backwards():
    donnie.bk(10)


def move_left():
    donnie.lt(10)


def move_right():
    donnie.rt(10)


def clear_screen():
    donnie.home()
    donnie.clear()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()