import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

# move turtle forward.
player = Player()
screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True

cnt = 0

car_mana = CarManager()
# trace score
score = Scoreboard()

while game_is_on:
    # make car and move right to left.
    if cnt % 6 == 0:
        car_mana.create_car()
    car_mana.move()
    time.sleep(0.1)
    screen.update()
    cnt += 1

    # if turtle arrived at goal line, reset the turtle's position and go to next level
    if player.go_next_level():
        # in next level car's speed is increased. 
        car_mana.increase_speed()
        score.increase_level()

    # if turtle crush with car, the game is ended.
    for car in car_mana.cars:
        if player.distance(car) <= 30:
            score.game_over()
            game_is_on = False

screen.exitonclick()