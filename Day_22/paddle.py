from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,position) -> None:
        super().__init__()
        self.color('white')
        self.shape('square')
        self.right(90)
        self.shapesize(stretch_len=5)
        self.penup()
        self.goto(position)
        
    def go_up(self):
        new_y = self.ycor() + 20 
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 20 
        self.goto(self.xcor(),new_y)
    