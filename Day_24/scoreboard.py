from turtle import Turtle
FONT = ('Arial', 12, 'normal')
ALIGNMENT = 'center'

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.score = 0
        with open('data.txt','r') as data:
            self.highscore = int(data.read())
        self.penup()
        self.goto(0,280)
        self.write(arg = f"Score: {self.score} Highscore: {self.highscore}", align = ALIGNMENT,font= FONT)

    def update_score(self):
        self.clear()
        self.write(arg = f"Score: {self.score}, Highscore: {self.highscore}", align = ALIGNMENT,font= FONT)
    
    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(arg = 'GAME OVER',align = ALIGNMENT,font = ('Arial', 20 , 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt','w') as data:
                data.write(str(self.highscore))
        self.score = 0
        self.update_score()



        
        
    