from turtle import Turtle

x_ball = 0
y_ball = 0

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#ffffff")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        #Cambia la direccion de la bola en el eje y multiplicandolo  por -1
        self.y_move *= -1

    def bounce_x(self):
        #Cambia la direccion de la bola multiplicandolo  por -1
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()





