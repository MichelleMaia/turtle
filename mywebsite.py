##########################################################################
# Author: Michelle Maia
# https://www.michellemaia.com
# https://www.youtube.com/user/MichelleAVCavalcanti
# Project: Exploring Turtle - Python
# Date: 08/23/2020
# Description: It shows some experiments with turtle module, like drawing
# some alphabet letters, changing a turtle to a gif image and drawing a bunch
# of circles. It also uses the random library to change colors and circle positions
# randomly.
#
# Source 1: https://docs.python.org/3/library/turtle.html#module-turtle
# Source 2: https://www.101computing.net/python-turtle-wordart-challenge/
# Source 3: https://trinket.io/python/52378ec006
# Source 4: https://youtu.be/p7CiFhiTdvY
##########################################################################

import turtle
import random
import math
from myalphabet import alphabet
import georgias_spirals

# Used colors
colors = ["red", "blue", "green", "purple", "yellow", "orange", "white"]

# Screen settings:
w_width = 1280
w_height = 700
window = turtle.Screen()
window.bgcolor("#000000")
window.setup(width=w_width, height=w_height)
window.register_shape("head.gif")


# Changing the size of "mi" Turtle
def mi_resize(n):
    mi.resizemode("user")
    mi.shapesize(n, n, n)


# Turtles settings:
mi = turtle.Turtle()
mi.setheading(90)
mi_resize(5)
mi.pensize(15)
mi.shape("turtle")
mi.speed(6)

turtle.hideturtle()
turtle.pencolor("white")
turtle.speed(0)


# Drawing the characters of the text
def display_message(message, font_size, speed, x0, y0):
    x = x0
    y = y0
    message = message.upper()

    mi.speed(10)
    mi.hideturtle()
    mi.penup()
    mi.goto(x, y)
    mi.showturtle()
    mi.speed(speed)

    for character in message:
        mi.color(random.choice(colors))
        if character in alphabet:
            letter = alphabet[character]
            mi.penup()
            a = b = 0
            for dot in letter:
                mi.setheading(math.degrees(math.atan2(dot[1] - b, dot[0] - a)))
                mi.goto(x + dot[0]*font_size, y + dot[1]*font_size)
                mi.pendown()
                a = dot[0]
                b = dot[1]

            x += font_size + 20

        elif character == '.':
            mi.penup()
            mi.setheading(0)
            mi.goto(x, y0)
            mi.pendown()
            mi.circle(5)
            x += 30


# Writing the message
def title(message):
    turtle.penup()
    turtle.setpos(0, (w_height/2)-100)
    turtle.write(message, move=False, align="center", font=("Arial", 60, "normal"))


# Drawing circles with a floating head
def floating_head(speed):
    # Turtles settings:
    xelle = turtle.Turtle()
    xelle.shape("head.gif")
    xelle.pensize(5)
    xelle.speed(speed)
    for x in range(3):
        rand_color1 = random.randrange(0, len(colors)-1)
        rand_color2 = random.randrange(0, len(colors)-1)
        xelle.color(colors[rand_color1], colors[rand_color2])
        rand1 = random.randrange(-(w_width//2)+100, (w_width//2)-100)
        rand2 = random.randrange(-(w_height//2)+100, (w_height//2)-100)
        xelle.penup()
        xelle.setpos((rand1, rand2))
        xelle.pendown()
        xelle.begin_fill()
        xelle.circle(random.randrange(30, 80))
        xelle.end_fill()
    xelle.penup()
    xelle.setpos((-w_width/2)+180, -30)


# Main Program Starts Here
# font size
size = 60

# It calls spirals function
color_spiral = list()
for i in range(5):
    rand_color = random.randrange(0, len(colors))
    color_spiral.append(colors[rand_color])
georgias_spirals.spirals(color_spiral, 6)

# It calls floating_head function to draw some circles
floating_head(8)

# It displays the text on screen
title("Learning Python is fun!!")

# It draws the website address
mi_resize(1)
display_message("michellemaia", size, 0, (-w_width/2)+250, -50)
display_message("www.", size, 0, (-w_width/2)+100, 100)
display_message(".com", size, 0, 300, -200)
mi_resize(2)
mi.forward(40)

# Command necessary to keep the window open
turtle.done()
