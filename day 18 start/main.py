import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)
tim.shape("turtle")
tim.color("red")
tim.pensize(9)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


tim.speed("fastest")
for _ in range(500):
    angle = random.choice([0, 90, 180, 270])
    color = random_color()
    tim.setheading(angle)
    tim.pencolor(color)
    tim.forward(25)




# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)

# sides = 3
# color = random.choice(["yellow", "blue", "red", "green", "purple", "brown", "black"])
#
#
# def draw_polygon():
#     for _ in range(sides):
#         tim.color()
#         tim.forward(100)
#         direction = 360/sides
#         tim.right(direction)
#
# for _ in range(10):
#     draw_polygon()
#     sides += 1























screen = Screen()
screen.exitonclick()
