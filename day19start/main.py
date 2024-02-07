import turtle
from turtle import Turtle, Screen
import  random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win the race? enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won! the {winning_color} turtle")
            else:
                print(f"you've lost! the {winning_color} turtle")
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)






# tim = Turtle(shape="turtle")
# tommy = Turtle(shape="turtle")
# temi = Turtle(shape="turtle")
# tolu = Turtle(shape="turtle")
# tayo = Turtle(shape="turtle")
# tim.color("orange")
# tommy.color("red")
# temi.color("yellow")
# tolu.color("green")
# tayo.color("purple")
# tim.penup()
# tommy.penup()
# temi.penup()
# tolu.penup()
# tayo.penup()
# tim.goto(x=-230, y=0)
# tommy.goto(x=-230, y=20)
# tayo.goto(x=-230, y=-60)
# temi.goto(x=-230, y=-20)
# tolu.goto(x=-230, y=-40)
#
#
#










screen.exitonclick()





