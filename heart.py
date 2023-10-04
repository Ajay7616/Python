import turtle
import pygame
pygame.init()
wn = turtle.Screen()
wn.setup(width=500, height=500)
red = turtle.Turtle()

def curveb():
    for i in range(200):
        red.right(1)
        red.forward(1.1)

def curvea():
    for i in range(200):
        red.right(1)
        red.forward(0.9)

def hearta():
    red.fillcolor('white')
    red.begin_fill()
    red.left(140)
    red.forward(113)
    curvea()
    red.left(120)
    curvea()
    red.forward(112)
    red.end_fill()

def heartb():
    red.fillcolor('red')
    red.begin_fill()
    red.left(140)
    red.forward(113)
    curveb()
    red.left(120)
    curveb()
    red.forward(112)
    red.end_fill()
    red.left(140)
pygame.mixer.init()
pygame.mixer.music.load('song.mp3')
pygame.mixer.music.play()

heartb()
hearta()
red.ht()
turtle.done()
