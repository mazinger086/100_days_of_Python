from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 200)
        self.color("#FFFFFF")
        self.ht()
        self.score_p1 = 0
        self.score_p2 = 0
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"{self.score_p2} | {self.score_p1}", False, align=ALIGNMENT, font=FONT)

    def r_point(self):
        self.score_p1 += 1
        self.update_score()

    def l_point(self):
        self.score_p2 += 1
        self.update_score()
