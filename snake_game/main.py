from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time


screen = Screen()
screen.setup(width=700, height=700)
screen.title("Snake Game")
screen.bgcolor("sky blue")

screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "s")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "a")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "d")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
    if snake.head.xcor() > 340 or snake.head.xcor() < -350 or snake.head.ycor() > 350 or snake.head.ycor() < -340:
        game_on = False
        score.reset()
        score.game_over()
    for segment in snake.snakes:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_on = False
            score.reset()
            score.game_over()
screen.exitonclick()
