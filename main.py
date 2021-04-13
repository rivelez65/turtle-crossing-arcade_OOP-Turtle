import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# SETUP SCREEN
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)

# SETUP CARS, TURTLE, SCOREBORAD AND STREET BACKGROUND
car = CarManager()
turtle = Player()
score = Scoreboard()
score.draw_walls()

# ACTIVATE KEY FUNCTIONALITY
screen.listen()
screen.onkey(key='Up', fun=turtle.move)
screen.onkey(key='Down', fun=turtle.move_back)

# VARIABLE LOOP COUNTER
loop_count = 0

# RUN GAME ON WHILE LOOP
game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()

    # SLOW DOWN CAR GENERATION GIVEN CAR LANES
    if loop_count % 12 == 0:
        car.top_lane()
        car.top_center_lane()
        car.bottom_center_lane()
    if loop_count % 20 == 0:
        car.bottom_lane()
    # REGULATE CAR SPEEDS
    car.move_fast(30)
    car.move_regular(20)
    car.move_slow(10)
    car.move_super_slow(5)

    # COUNT LOOP
    loop_count += 1

    # TRACK EACH CAR'S INDIVIDUAL POSITION
    for item in range(len(car.master_list)):
        y = car.master_list[item].ycor()
        x = car.master_list[item].xcor()
        turtle_y = turtle.player.ycor()
        turtle_x = turtle.player.xcor()
        y_dif = y - turtle_y
        x_dif = x - turtle_x

        # ADD SCORE IF TURTLE REACHES OTHER SIDE OF THE HIGHWAY AND TAKE TURTLE BACK TO START
        if turtle_y == 250:
            score.increase_score()
            turtle.player.goto(500, 250)
            turtle.player.goto(500, -250)
            turtle.player.goto(0, -250)

        # GAME OVER IF A COLLISION IS DETECTED
        if -20 < y_dif < 20 and -20 < x_dif < 20:
            game_is_on = False
            score.game_over()


screen.exitonclick()
