#!/usr/bin/python -tt
import turtle

window = turtle.Screen()
window.setup(width=500, height=500, startx=None, starty=None)
window.bgcolor("black")
colors = ["red", "blue", "yellow", "green"] #palette for .pencolor method

class Geoturtle(turtle.Turtle):
    def __init__(self, *args, **kwargs):
        super(Geoturtle, self).__init__(*args, **kwargs)
       
    def draw_square(self):

        for i in range(0, 4, 1):
            self.pencolor(colors[i])
            self.forward(100)
            self.right(90)

    def draw_circle(self):
        for i in range(0, 4, 1):
            self.pencolor(colors[i])
            self.circle(50, 90)


    def draw_triangle(self):
            self.pencolor(colors[0])
            self.forward(-100)
            self.left(60)
            self.pencolor(colors[1])
            self.forward(100)
            self.left(60)
            self.pencolor(colors[2])
            self.forward(-100)

objA = Geoturtle()
objA.setpos(-50, -60)
objA.ht() #hide 



for i in range(0, 360, 1):
    objA.draw_square()
    objA.right(1)

##objB = Geoturtle()
##objB.setpos(0, -40)
##objB.ht()
##
##objC = Geoturtle()
##objC.setpos(50, 80)
##objC.ht()
##
##objA.draw_square()
##objB.draw_circle()
##objC.draw_triangle()
