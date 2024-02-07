import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
scoreboard = Scoreboard()

car_managers = []
screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
count = 0


while game_is_on:
    count += 1
    time.sleep(0.1)
    screen.update()
    if count % 6 == 0:
        car_manager = CarManager()
        car_managers.append(car_manager)
    for car_manager in car_managers:
        car_manager.movement()
        car_coord = (car_manager.xcor(), car_manager.ycor())
        # fin ishing line
        if player.distance(car_coord) < 20:
            game_is_on = False
            scoreboard.game_over()
        if player.is_at_end():
            player.goto_default()
            car_manager.level_up()
            scoreboard.increase_level()





