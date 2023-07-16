from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

WIDTH = 800
HEIGHT = 600
SCREEN_COLOR = "#222222"


screen = Screen()
screen.bgcolor(SCREEN_COLOR)
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("PONG Game")
#Con el tracer apagas la animacion cuendo esta en 0
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')

screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    # Con el update la mostras la animacion que apagaste con tracer
    screen.update()
    ball.move()

    #Detect collision with top or bottom wall
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect if R paddle misses
    if ball.xcor() > 400:
        # game_is_on = False
        ball.reset_position()
        scoreboard.l_point()



    # Detect if L paddle misses
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()





screen.exitonclick()


