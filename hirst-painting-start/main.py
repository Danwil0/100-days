# import colorgram
# from PIL import Image
#
# image_path = r'C:\Users\dweezyfc\Downloads\hirst-painting-start\image.jpg'
#
# image = Image.open(image_path)
#
#
# color = colorgram.extract(image, 30)
# color_list = []
#
# for colors in color:
#     color_tuple = tuple(colors.rgb)
import random
#     color_list.append(color_tuple)
# print(color_list)
import turtle as turtle_module
from turtle import Screen
turtle_module.colormode(255)
tim = turtle_module.Turtle()

color_palette = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_palette))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(58)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)






# space = 10
# def tenby():
#     for _ in range(10):
#         tim.dot(20)
#         tim.penup()
#         tim.forward(50)
# for _ in range(9):
#     tenby()
#     tim.left(90)
#     tim.forward(20)
#     tim.left(90)
#     tim.forward(20)
#     tim.pendown()
#     tenby()
#     tim.right(90)
#     tim.forward(20)
#     tim.right(90)
# # for _ in range(10):
#     tim.penup()
#     tim.dot(10)
#     tim.forward(26)

# lines = 5
# separation = 10

# Loop through the number of lines
# for i in range(lines):
#   # Draw a line
#   tim.forward(100)
#   # Move the turtle up by the separation distance
#   tim.penup()
#   tim.setheading(90)
#   tim.forward(separation)
#   tim.pendown()
#   # Move the turtle back to the starting point of the next line
#   tim.setheading(180)
#   tim.forward(100)
#   tim.setheading(0)











screen = Screen()
screen.exitonclick()

