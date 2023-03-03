from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 0.5
MOVE_INCREMENT = 1


class CarManager():
    
    def __init__(self) -> None:
        self.car_fleet = []
        self.moving_distance = STARTING_MOVE_DISTANCE

    def new_car(self):
        new_car = Turtle()
        new_car.color(random.choice(COLORS))
        new_car.shape('square')
        new_car.shapesize(stretch_len= 2)
        new_car.penup()
        new_car.goto(300,random.randint(-250,250))
        new_car.moving_distance = STARTING_MOVE_DISTANCE
        self.car_fleet.append(new_car)

    def move_cars(self):
        for car in self.car_fleet:
            new_x = car.xcor() - self.moving_distance
            car.goto((new_x,car.ycor()))

    def increase_moving_distance(self):
        self.moving_distance += MOVE_INCREMENT

    def collision_detector(self,player):
        collision = False
        for car in self.car_fleet:
            if car.distance(player)< 27:
                collision = True
        return collision

    
