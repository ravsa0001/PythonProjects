from turtle import Screen
import time
from snakec import Snake
from food import Food
from food import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()

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
    
    if snake.head.distance(Food) < 15:
        Food.refresh()
        snake.extend()
        Scoreboard.incsc()
        
    if snake.head.xcor() > 280 or snake.head.xcor() > -280 or snake.head.ycor() > 280 or snake.head.ycor() > -280:
        game_on = False
        
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_on = False
            Scoreboard.game_over()


screen.exitonclick()