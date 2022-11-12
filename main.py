import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#initialise environment
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()
scoreboard = Scoreboard()

#configure screen behaviour
screen.listen()
screen.onkey(player.movement, "Up")



game_is_on = True


while game_is_on:

    time.sleep(0.1)
    screen.update()


    #generate random cars in random colours
    cars.generate_cars()
    cars.car_movement()


    if player.ycor() >= 280 :
        player.reset_position()
        scoreboard.level_increase()
        scoreboard.update_level()
        cars.increase_speed()

    # detect collision of turtle with traffic
    for i in cars.traffic :
        if i.distance(player) <= 20 :
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()














