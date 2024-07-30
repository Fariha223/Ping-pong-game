import time
from turtle import Screen
from paddle import Paddle
from pong_scoreboard import Scoreboard
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect r paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # detect l paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
