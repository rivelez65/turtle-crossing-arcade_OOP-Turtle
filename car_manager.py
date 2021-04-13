from random import randint, choice
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "white"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
fast_list = []
regular_list = []
slow_list = []
super_slow = []


class CarManager:

    def __init__(self):
        self.random_y = randint(-220, 220)
        self.master_list = []

    def car_generator(self):
        self.car = Turtle()
        self.car.shape('square')
        self.car.color(choice(COLORS))
        self.car.shapesize(1, 2)
        self.car.speed('fastest')
        self.car.penup()

    def top_lane(self):
        self.random_y = randint(135, 220)
        self.car_generator()
        self.car.goto(-300, self.random_y)
        self.car.setheading(0)
        self.random_y = randint(135, 220)
        fast_list.append(self.car)
        self.master_list.append(self.car)

    def top_center_lane(self):
        self.random_y = randint(0, 134)
        self.car_generator()
        self.car.goto(-300, self.random_y)
        self.car.setheading(0)
        self.random_y = randint(0, 134)
        regular_list.append(self.car)
        self.master_list.append(self.car)

    def bottom_center_lane(self):
        self.random_y = randint(-134, -1)
        self.car_generator()
        self.car.goto(-300, self.random_y)
        self.car.setheading(0)
        self.random_y = randint(-134, -1)
        slow_list.append(self.car)
        self.master_list.append(self.car)

    def bottom_lane(self):
        self.random_y = randint(-220, -135)
        self.car_generator()
        self.car.goto(-300, self.random_y)
        self.car.setheading(0)
        self.random_y = randint(-220, -135)
        super_slow.append(self.car)
        self.master_list.append(self.car)

    def move_fast(self, speed):
        for x in range(len(fast_list)):
            fast_list[x].forward(speed)

    def move_regular(self, speed):
        for x in range(len(regular_list)):
            regular_list[x].forward(speed)

    def move_slow(self, speed):
        for x in range(len(slow_list)):
            slow_list[x].forward(speed)

    def move_super_slow(self, speed):
        for x in range(len(super_slow)):
            super_slow[x].forward(speed)
