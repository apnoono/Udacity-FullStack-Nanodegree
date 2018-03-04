#!/usr/bin/python -tt

import turtle

class Turtle (turtle.Turtle):

    def draw_L(xvalue):
            this.pencolor("red")
            this.forward(xvalue)
            this.right(90)
            this.pencolor("blue")
            this.forward(xvalue)
            this.right(90)
            this.up()
            this.setpos(0, 0)
                
    def draw_square(xvalue):
        for i in range(2, 0, -1):
            this.pencolor("red")
            this.forward(xvalue)
            this.right(90)
            this.pencolor("blue")
            this.forward(xvalue)
            this.right(90)

    def draw_picture():
        for i in range(45, 0, -1):
            bart.draw_L(-100)
            brad.draw_L(100)
            brad.right(1)
            bart.right(1)  
        window.exitonclick()
        
window = turtle.Screen()
window.bgcolor("black")

brad = turtle.Turtle()
brad.shape("turtle")
brad.speed(0)
brad.ht()

bart = turtle.Turtle()
bart.shape("turtle")
bart.speed(0)
bart.ht()


brad.turtle__draw_L(100)
