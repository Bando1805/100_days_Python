from turtle import Turtle, Screen

screen = Screen()
screen.setup(width = 500 , height = 400)
user_guess = screen.textinput(title = 'Make your bet', prompt = 'Which turtle will win the race? Enter a color : ')
colors = ['red','orange','yellow','green','blue','purple']
position_y = list(range(-70,81,30))
all_turtle=[]
for i in range(6):
    new_turtle = Turtle(shape = 'turtle')
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x = -230,y = position_y[i])
    all_turtle.append(new_turtle)

print(all_turtle)


screen.exitonclick()