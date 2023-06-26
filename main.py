from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake=Snake()
food=Food()
scoreboard=Scoreboard()

game_on=True

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

while game_on==True:
    screen.update()
    time.sleep(0.1)
    snake.move()  

    # detecting collision of food 
    if snake.head.distance(food) < 15:
        food.create_food()
        scoreboard.increase_score()
        snake.enlarge_snake()

    # detect collision with wall 
    if snake.head.xcor()>290 or snake.head.ycor()>290 or snake.head.xcor()<-290 or snake.head.ycor()<-290:
        # game_on=False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()
    
    # detection of collision with its tail
    for segments in snake.segments[1:-1]:
        if snake.head.distance(segments)<10:
            # game_on=False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()

screen.exitonclick()