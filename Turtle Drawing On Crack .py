# Signing in 

import turtle
import random

colors = ['red', 'blue', 'green', 'purple', 'orange']

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor('black')

for i in range(100):
    t.color(random.choice(colors))
    t.forward(i * 2)
    t.left(91)

turtle.done()

# Try not to hypnotize yourself😂
# Signing off 
