from turtle import Screen, Turtle
import random as r
from snake import Snake
from food import Food
from scoreboard import Scoreboard


if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    snake = Snake(screen)
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.go_up, "Up")
    screen.onkey(snake.go_down, "Down")
    screen.onkey(snake.go_left, "Left")
    screen.onkey(snake.go_right, "Right")

    game_is_on = True
    while game_is_on:
        snake.animation()

        if snake.head.distance(food) < 15:
            food.position()
            snake.add_length()
            scoreboard.increase_score()

        if (snake.head.xcor() > 300) or (snake.head.ycor() > 300) or (snake.head.xcor() < -300) or (snake.head.ycor() < -300): 
            game_is_on = False
            scoreboard.game_over()

        for part in snake.snake_parts:
            if part == snake.head: pass
            elif snake.head.distance(part) < 10:
                game_is_on = False
                scoreboard.game_over()

    screen.exitonclick()