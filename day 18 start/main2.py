import turtle
from turtle import Turtle, Screen
import random
t = Turtle()

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


t.speed("fastest")


def draw(sizeg):
    for _ in range(int(360/sizeg)):
        t.pencolor(random_color())
        t.circle(100)
        t.setheading(t.heading() + sizeg)

draw(5)

























screen = Screen()
screen.exitonclick()