from turtle import Turtle
FONT = ('Arial', 12, 'normal')
ALIGNMENT = 'center'

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.score = 0
        self.penup()
        self.goto(0,280)
        self.write(arg = f"Your score is {self.score}", align = ALIGNMENT,font= FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg = f"Your score is {self.score}", align = ALIGNMENT,font= FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write(arg = 'GAME OVER',align = ALIGNMENT,font = ('Arial', 20 , 'normal'))
        
        
    