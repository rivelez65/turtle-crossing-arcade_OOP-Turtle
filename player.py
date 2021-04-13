from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:

    def __init__(self):
        self.player = Turtle()
        self.player.shape('turtle')
        self.player.color('white')
        self.player.penup()
        self.player.goto(STARTING_POSITION)
        self.player.setheading(90)

    def move(self):
        self.player.forward(MOVE_DISTANCE)

    def move_back(self):
        self.player.backward(MOVE_DISTANCE)
