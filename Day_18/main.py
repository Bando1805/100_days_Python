import turtle as t
import random
import colorgram


t.colormode(255)
# Extract 6 colors from an image.
colors = colorgram.extract('image.jpg', 100)
colors_dots =[]
for item in colors:
    r = item.rgb.r
    g = item.rgb.g
    b = item.rgb.b
    rgb_color = (r,g,b)
    colors_dots.append(rgb_color)

tim = t.Turtle()
tim.speed('fastest')
tim.up()
tim.goto((-230,230))

for i in range(10):
    for j in range(10):
        tim.color(random.choice(colors_dots))
        tim.down()
        tim.begin_fill()
        tim.circle(10)
        tim.end_fill()
        tim.up()
        position = tim.position()
        tim.setx(position[0]+50)
    
    position = tim.position()
    tim.setx(position[0] - 500)
    tim.sety(position[1] - 50)

    
 


screen = t.Screen()
screen.exitonclick()