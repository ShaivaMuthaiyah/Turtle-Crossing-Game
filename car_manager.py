from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_NUMBER = 25

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.traffic = []
        



    def generate_cars(self):
        number = random.randint(1, 6)

        if number == 1 :
            x_position = 300
            random_y = random.randint(-230, 230)
            car = Turtle("square")
            car.shapesize(1, 2)
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(x_position,random_y)
            self.traffic.append(car)


    def car_movement(self):

        for car in self.traffic :
            y_position = car.ycor()
            x_position = car.xcor()
            new_xposition = x_position - self.car_speed
            car.goto(new_xposition, y_position)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

