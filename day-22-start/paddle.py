from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("#FFFFFF")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.sety(new_y)

    def go_down(self):
        if self.ycor() > -230:
            new_y = self.ycor() - 20
            self.sety(new_y)
