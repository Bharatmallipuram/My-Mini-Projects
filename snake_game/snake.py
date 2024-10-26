from turtle import Turtle, Screen

screen = Screen()
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
I = [(0, 0), (-20, 0), (-40, 0)]


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snakes = []
        self.hideturtle()
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in I:
            self.add_segment(position)

    def add_segment(self, position):
        new_snake = Turtle("circle")
        new_snake.color("green")
        new_snake.penup()
        new_snake.goto(position)
        self.snakes.append(new_snake)

    def extend(self):
        self.add_segment(self.snakes[-1].position())

    def move(self):
        for seg in range(len(self.snakes)-1, 0, -1):
            new_x = self.snakes[seg-1].xcor()
            new_y = self.snakes[seg - 1].ycor()
            self.snakes[seg].goto(new_x, new_y)
        self.snakes[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
