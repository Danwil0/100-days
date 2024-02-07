
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

#
# class CarManager(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.car_speed = STARTING_MOVE_DISTANCE
#         self.penup()
#         self.shape("square")
#         self.color(random.choice(COLORS))
#         self.shapesize(stretch_wid=1, stretch_len=2)
#         self.y_random_pos = random.randint(-250, 270)
#         self.x_random_pos = random.randint(320, 330)
#         self.setheading(180)
#         self.setpos(self.x_random_pos, self.y_random_pos)
#         self.coord = ()
#
#     def movement(self):
#         self.forward(self.car_speed)
#         self.coord = (self.xcor(), self.ycor())
#
#     def level_up(self):
#         self.car_speed += MOVE_INCREMENT


class CarManager(Turtle):
    car_speed = STARTING_MOVE_DISTANCE

    def __init__(self):
        super().__init__()

        self.penup()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.y_random_pos = random.randint(-250, 250)
        self.x_random_pos = random.randint(320, 330)
        self.setheading(180)
        self.setpos(self.x_random_pos, self.y_random_pos)
        self.coord = ()

    def movement(self):
        self.forward(CarManager.car_speed)
        self.coord = (self.xcor(), self.ycor())

    def level_up(self):
        CarManager.car_speed += MOVE_INCREMENT



