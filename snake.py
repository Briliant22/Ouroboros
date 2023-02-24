from turtle import Turtle
import time
import random as r

class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.snake_parts = []
        self.snake_length = 3
        self.create_snake()
        self.head = self.snake_parts[0]

    def create_snake(self):
        for i in range(self.snake_length):
            snake_part = Turtle(shape="square")
            snake_part.color("white")
            snake_part.penup()
            snake_part.goto(x=-10 - (i * 20) , y=0)
            self.snake_parts.append(snake_part)

    def animation(self):
        time.sleep(0.1) 
        self.screen.update()

        for body in self.snake_parts[-1:0:-1]:
            body.goto(x=self.snake_parts[self.snake_parts.index(body)-1].xcor() , y=self.snake_parts[self.snake_parts.index(body)-1].ycor())

        self.head.fd(20)

    def add_length(self):
        new_part = Turtle("square")
        new_part.color("white")
        new_part.penup()
        new_part.goto(self.snake_parts[-1].position())
        self.snake_parts.append(new_part)

    def go_right(self):
        self.head.setheading(0)

    def go_up(self):
        self.head.setheading(90)

    def go_left(self):
        self.head.setheading(180)

    def go_down(self):
        self.head.setheading(270)