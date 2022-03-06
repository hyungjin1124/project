# create the screen
from turtle import Screen, left, right
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("pong")

is_game_on = True

# create and move a paddle
screen.tracer(0)
right_paddle = Paddle((350, 0))
# create another paddle
left_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

# create the ball and make it move
ball = Ball()

# keep score
score = Score()

while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    current_x = ball.xcor()
    ball.move()
    # detect collision with wall and bounce
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # detect collision with paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 330) or ball.distance(left_paddle) <= 50 and ball.xcor() <= -330:
        ball.bounce_x()
        print(ball.move_speed)

    # detect when paddle misses 
    if ball.xcor() >= 390:
        score.get_score('left')
        ball.reset_position()
        score.update_score()

    if ball.xcor() <= -390:
        score.get_score('right')
        ball.reset_position()
        score.update_score()

screen.exitonclick()
