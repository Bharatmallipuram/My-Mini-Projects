from turtle import Screen
from paddles import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=700, height=600)
screen.title("Ping Pong")
screen.bgcolor("black")
screen.tracer(0)

left_p = Paddle((-330, 0))
right_p = Paddle((320, 0))
ball = Ball()
score = Score()

screen.listen()

screen.onkey(left_p.up, "w")
screen.onkey(left_p.down, "s")
screen.onkey(right_p.up, "Up")
screen.onkey(right_p.down, "Down")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # for wall bounce...
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # for paddle bounce...
    if (ball.distance(right_p) < 30 and ball.xcor() > 290) or (ball.distance(left_p) < 30 and ball.xcor() < -290):
        ball.bounce_x()

    if ball.xcor() > 330:
        score.l_point()
        ball.reset_position()

    if ball.xcor() < -330:
        score.r_point()
        ball.reset_position()


screen.exitonclick()
