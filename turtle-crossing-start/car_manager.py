from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.move_distance = STARTING_MOVE_DISTANCE
        self.cars = []

    def create_car(self):
        new_car = Turtle("square")
        new_car.penup() 
        new_car.color(random.choice(COLORS))
        new_car.shapesize(1, 2)
        new_car.goto(290, random.randint(-250, 250))
        self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.move_distance)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT

