from turtle import Screen
import time

from food import Food
from snake import Snake
from score import Score

screen = Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detecting collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.update_score()
        snake.extend_snake()

    # detecting collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()


    # detecting collision of snake head with snake body

    for segment in snake.segments:

        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10 :
            game_on = False
            score.game_over()
screen.exitonclick()
