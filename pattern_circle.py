import turtle
t = turtle.Turtle()
t.screen.bgcolor('black')
t.speed(1)
t.pensize(2)

color = ['pink','hotpink','deeppink','palevioletred']
for x in range (150):
    t.color(color [x % 4])
    t.circle(x) 
    t.left(30)

t.hideturtle()
turtle.done()