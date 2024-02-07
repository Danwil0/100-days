from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard
import time

screen = Screen()
screen.title("PONG GAME")
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

score_board = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_on = True
while game_on:
    time.sleep(ball.difficulty)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()

    # paddle collision
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # missing right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.l_point()

    # missing left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()
















screen.exitonclick()

