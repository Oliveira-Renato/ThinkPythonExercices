import math
import turtle

bob = turtle.Turtle()

""" the function square will draw a square. Pretty obvious
    t = turtle
"""
def square(t, length):
    for y in range(4):
        t.fd(length)
        t.lt(90)

""" the function polygon will draw a polygon. Pretty obvious
    n = 360/n will provide the polygon exterior angles
"""
def polygon(t, length, n):
    for y in range(n):
        t.fd(length)
        t.lt(360/n)

""" the function circle will draw an approximate circle by calling polygon.
    r = is the radious of the circle
    16 is the length of this circle
"""
def circle(t, r):
    area = math.pi * math.pow(r,2)
    #circumference = math.pi * 16
    polygon(t, area, 16)

""" the function arc will draw a general circle by taking another parameter angle.
"""    
def arc(t, r, length, angle):
    area = math.pi * math.pow(r,2)
    #circumference = math.pi * 16
    
    for y in range(angle):
        t.fd(length)
        t.lt(360/area)
        

square(bob, 100)
polygon(bob, length=100, n=6)
circle(bob, 4)
arc(bob, r=4, length=16, angle=51)

