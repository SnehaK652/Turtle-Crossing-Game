import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

score=Scoreboard()
player1=Player()
player1.update_turtle()
game_is_on = True

car = CarManager()

while game_is_on:
    time.sleep(0.1)
    score.levels()

    screen.update()
    screen.listen()
    screen.onkey(player1.move_turtle,"Up")
    car.car_default()
    car.car_move()

    for r in car.all_cars:
      if player1.distance(r) < 20:
        game_is_on=False
        score.clear()
        score.game_over()
    if player1.Finish():
        player1.goto_start()
        score.scores()
        car.level_up()









screen.exitonclick()