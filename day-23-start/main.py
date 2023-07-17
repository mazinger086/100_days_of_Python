import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

p1 = Player()
car_manager = CarManager()
score = Scoreboard()


screen.listen()
screen.onkey(p1.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1) # Se llama cada 1 milesima de seg
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(p1) < 20:
            score.game_over()
            game_is_on = False

    #Detect if the turtle cross sucessfully
    if p1.is_at_finish_line():
        p1.go_to_start()
        car_manager.level_up()
        score.add_level()





screen.exitonclick()
