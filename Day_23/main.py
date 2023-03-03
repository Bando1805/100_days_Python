import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move,'space')

game_loop_run = 0
game_is_on = True
while game_is_on:
    scoreboard.show_level()
    game_loop_run += 1
    if game_loop_run % 60 == 0:
        car_manager.new_car()
    
    car_manager.move_cars()
    
    if car_manager.collision_detector(player):
        game_is_on = False 
        scoreboard.game_over()
    
    if player.level_completed():
        scoreboard.level += 1
        car_manager.increase_moving_distance()

    
    time.sleep(0.01)
    screen.update()


screen.exitonclick()