#import turtle
#timmy = turtle.Turtle()

# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("cyan")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

import prettytable
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("pokemon name",
                 ["pikachu", "squirtle", "charmander"]
                 )
table.add_column("type",
                 ["electric", "water", "fire"]
                 )
table.align = "l"
print(table)



