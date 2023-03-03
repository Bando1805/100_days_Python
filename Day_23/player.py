from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.shape('turtle')
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        new_x = self.xcor()
        new_y = self.ycor() + MOVE_DISTANCE 
        self.goto((new_x,new_y))

    def level_completed(self):
        level_finished = False
        if self.ycor() == FINISH_LINE_Y:
            level_finished = True
            self.goto(STARTING_POSITION)
        return level_finished
    
    

    

    
