##########################################################################
# Author: Michelle Maia
# https://www.michellemaia.com
# Project: Turtle exploring
# Date: 08/23/2020
# Source 1: https://docs.python.org/3/library/turtle.html#module-turtle
# Source 2: https://www.101computing.net/python-turtle-wordart-challenge/
# Source 3: https://trinket.io/python/52378ec006
# Source 4: https://youtu.be/p7CiFhiTdvY
##########################################################################

import turtle


def draw_circles(t, size, option):
    for i in range(10):
        t.circle(size)
        size -= option


def draw_special(t, size, repeat, option):
    for i in range(repeat):
        draw_circles(t, size, option)
        t.right(360 / repeat)


def spirals(color, repetition):
    albert = turtle.Turtle()
    albert.hideturtle()
    albert.speed(0)
    albert.color(color[0])
    draw_special(albert, 100, repetition, 4)
    albert.color(color[1])
    draw_special(albert, 100, repetition, 10)
    albert.color(color[2])
    draw_special(albert, 100, repetition, 5)
    albert.color(color[3])
    draw_special(albert, 100, repetition, 19)
    albert.color(color[4])
    draw_special(albert, 100, repetition, 20)
