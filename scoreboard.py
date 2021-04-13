from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('blue')
        self.hideturtle()
        self.penup()
        self.goto(-240, 270)
        self.update_score()

    def update_score(self):
        self.write(f"SCORE: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER!!!!!!", align=ALIGNMENT, font=FONT)
        self.goto(0, 50)
        self.update_score()

    def draw_walls(self):
        t = Turtle()
        t.penup()
        t.color("yellow")
        t.pensize(2)
        t.goto(280, -250)
        t.pendown()
        t.goto(-280, -250)
        t.penup()
        t.goto(-280, 250)
        t.pendown()
        t.goto(280, 250)
        t.penup()
        t.goto(280,135)
        t.pendown()
        t.color('white')
        t.setheading(180)
        for x in range(20):
            t.forward(10)
            t.penup()
            t.forward(20)
            t.pendown()
        t.penup()
        t.goto(-280, 0)
        t.pendown()
        t.setheading(0)
        for x in range(20):
            t.forward(10)
            t.penup()
            t.forward(20)
            t.pendown()
        t.penup()
        t.goto(280, -135)
        t.pendown()
        t.setheading(180)
        for x in range(20):
            t.forward(10)
            t.penup()
            t.forward(20)
            t.pendown()
        t.hideturtle()
