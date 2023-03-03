from turtle import Turtle
PERC_SPEED_INCREASE = 0.2

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10

 
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
    
    def bounce_y(self):
        self.y_move *= - (1+ PERC_SPEED_INCREASE)

    def bounce_x(self):
        self.x_move *= -(1+ PERC_SPEED_INCREASE)

    def reset_position(self):
        self.goto(0,0)
        self.reset_speed()
    
    def reset_speed(self):
        self.x_move = (- self.x_move / abs(self.x_move) ) * 10
        self.y_move = (- self.x_move / abs(self.x_move) ) * 10




