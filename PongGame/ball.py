from turtle import Turtle
import random
dist = random.randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.nx = 0
        self.ny = 0
        self.x_new_move = 10
        self.y_new_move = 10
        self.difficulty = 0.1

    def move_ball(self):
        self.nx = self.xcor() + self.x_new_move
        self.ny = self.ycor() + self.y_new_move
        self.goto(self.nx, self.ny)

    def bounce_y(self):
        # self.setpos(self.nx, self.ny)
        self.y_new_move *= -1
        self.difficulty *= 0.9fault

    def bounce_x(self):
        self.x_new_move *= -1
        self.difficulty *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.difficulty = 0.1
        self.bounce_x()












