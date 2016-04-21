'''A simple graphics example constructs a face from basic shapes.
'''

from graphics import *
from math import sin,cos,radians
s = []



win = GraphWin('Map', 1200, 600) # give title and dimensions
#win.yUp() # make right side up coordinates!
f = open('DistanceTrue.csv', 'r')
for line in f:
    s.append(line.rstrip().split(','))
del s[0]

for i in range(len(s)):
    s[i][1] = float(s[i][1])
    s[i][0] = -float(s[i][0])


original = Point(600, 300) # set original point
original.draw(win)
for i in range(len(s)):
    values = s[i]
    if i == 0:
        x0 = 600
        y0 = 300

    x1 = sin(radians(float(values[0])))*float(values[1])
    y1 = cos(radians(float(values[0])))*float(values[1])
    Line(original, Point(x1+x0,y1+y0)).draw(win)

    #if not (values == s[0]):
    original = Point(x1+x0,y1+y0)
    x0 += x1
    y0 += y1
    #message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
    #message.draw(win)
win.getMouse()
while True:
    a=0
win.close()
