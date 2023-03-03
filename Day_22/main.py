from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width= 800,height= 600)
screen.bgcolor('black')
screen.title('paddle')
screen.tracer(0)




paddle_r = Paddle((350,0))
paddle_l = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_r.go_up,'Up')
screen.onkey(paddle_r.go_down,'Down')
screen.onkey(paddle_l.go_up,'w')
screen.onkey(paddle_l.go_down,'s')

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.1)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if (ball.xcor() > 320 and ball.distance(paddle_r) < 50) or (ball.xcor() < -320 and ball.distance(paddle_l) < 50 ):
        ball.bounce_x()

    #detect R paddle missing
    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.l_scores()
        
    
    #detect L paddle missing 
    if ball.xcor() < -380 :
        ball.reset_position()
        scoreboard.r_scores()
        
















screen.exitonclick()