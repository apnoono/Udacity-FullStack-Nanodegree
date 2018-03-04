#!/usr/bin/python -tt
import turtle
from turtle import *
colors = ["red", "blue", "yellow", "green"] #palette for .pencolor method

"""
This program generates fractal curve designs
using affine transforms:
(1) A Barnsley-like curve using affine transformations

"""


class FractalTurtle(turtle.Turtle):
    # Example derived from Barnsely Fern in Python 3
    # https://solarianprogrammer.com/2017/11/02/barnsley-fern-python-3/
    # Further information on Barnsely's Fern found here:
    # http://mathworld.wolfram.com/BarnsleysFern.html
    def __init__(self, *args, **kwargs):
        super(FractalTurtle, self).__init__(*args, **kwargs)
        self.curve = self.Barnsley()

    class Barnsley:
        def __init__(self, coefficients="fern"):
            self.nr_points = 10000

            #Initial (starting point)
            self.x = 0.0
            self.y = 0.0

            # Store the Fractal points
            self.point_x = []
            self.point_y = []
  
            # Select the set of coefficients to use
            if coefficients == "fern":
                self.probability_factors = [0.01, 0.85, 0.07, 0.07]
                self.a = [0, 0.85, 0.20, -0.15]
                self.b = [0, 0.04, -0.26, 0.28]
                self.c = [0, -0.04, 0.23, 0.26]
                self.d = [0.16, 0.85, 0.22, 0.24]
                self.e = [0, 0, 0, 0]
                self.f = [0, 1.6, 1.6, 0.44]

            self.nr_transforms = len(self.probability_factors)
            # Cumulative sum of the probability factors,
            # this defines the intervals corresponding to each transform
            self.cumulative_probabilities = [0] * (self.nr_transforms + 1)
            for i in range(1, len(self.cumulative_probabilities)):
                self.cumulative_probabilities[i] = self.cumulative_probabilities[i - 1] + \
                                                   self.probability_factors[i - 1]

        def select_transform(self):
            import random
            """Randomly select an affine transform"""
            rnd = random.random()
            for i in range(self.nr_transforms):
                if self.cumulative_probabilities[i] <= rnd <= self.cumulative_probabilities[i + 1]:
                    self.current_transform = i
                    break

        def next_point(self):
            """Get the next point of the fractal"""
            self.select_transform()
            x_new = self.a[self.current_transform] * self.x + self.b[self.current_transform] * self.y + self.e[self.current_transform]
            y_new = self.c[self.current_transform] * self.x + self.d[self.current_transform] * self.y + self.f[self.current_transform]
            self.x = x_new
            self.y = y_new
            self.point_x.append(x_new)
            self.point_y.append(y_new)

        def generate_points(self):
            """Generate all the fractal points"""
          
            for _ in range(self.nr_points):
                self.next_point()

                # Bounding box for the fractal
                self.x_min = min(self.point_x)
                self.x_max = max(self.point_x)
                self.y_min = min(self.point_y)
                self.y_max = max(self.point_y)

def main():
    # Initialize the fractal data and turtle
    artist = FractalTurtle()
    artist.ht() #hides turtle
    artist.getscreen().tracer(25,10)
    artist.curve.generate_points()
    artist.pencolor("green")
    artist.setheading(0)
    window = turtle.Screen()
    window.title("Barnsley's Fern Fractal Demo")
    window.bgcolor("#000000")
    # Background photo by Levi XU on Unsplash
    # https://unsplash.com
    window.bgpic("levi-xu-125529-unsplash-copy.gif")
    window.setup(width=500, height=500, startx=None, starty=None)

    #Define the image size and scale factor
    img_width = 250
    img_height = 250
    scale = min([img_height/(artist.curve.y_max - artist.curve.y_min), img_width/(artist.curve.x_max - artist.curve.x_min)]) * 0.9

    print(artist.fillcolor())
    print(artist.heading())


    # For every point of the fractal data, transform the point in the image
    # and fill the pixel color
    for i in range(10000):
        x = int((artist.curve.point_x[i] - artist.curve.x_min) * scale) + int((img_width - (artist.curve.x_max - artist.curve.x_min) * scale)/2)
        print("x: " + str(x))
        y = -int((artist.curve.point_y[i] - artist.curve.y_min) * scale) + int((img_height - (artist.curve.y_max - artist.curve.y_min) * scale)/2)
        print("y: " + str(y))
        artist.pu()
        artist.setpos(x, y)
        artist.pd()
        artist.forward(.5)

    window.exitonclick()
# Draw the image
if __name__ == "__main__":
    main()
