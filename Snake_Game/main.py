from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
food=Food()
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)
sb=Scoreboard()
snake=Snake()
screen.listen()
screen.onkey(fun=snake.move_up,key="Up")
screen.onkey(fun=snake.move_rt,key="Right")
screen.onkey(fun=snake.move_dn,key="Down")
screen.onkey(fun=snake.move_lt,key="Left")
game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Collision detection with food
    if snake.head.distance(food)<15:
        food.refresh_loc()
        snake.extend_snake()
        sb.increase_scoreboard()
    sb.update_scoreboard()

    # Collision detection with wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        game_on=False
        sb.clear()
        sb.game_over()

    # Collision detection with tail
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            game_on = False
            sb.clear()
            sb.game_over()




screen.exitonclick()