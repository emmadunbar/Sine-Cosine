"""
sinecosine.py
Author: Emma Dunbar
Credit: none

Assignment:

In this assignment you must use *list comprehensions* to generate sprites that show the behavior
of certain mathematical functions: sine and cosine. 

The sine and cosine functions are provided in the Python math library. These functions are used
to relate *angles* to *rectangular* (x,y) coordinate systems and can be very useful in computer
game design.

Unlike the last assignment using ggame`, this one will not provide any "skeleton" code to fill
in. You should use your submission for the Picture assignment 
(https://github.com/HHS-IntroProgramming/Picture) as a reference for starting this assignment. 

See:
https://github.com/HHS-IntroProgramming/Sine-Cosine/blob/master/README.md
for a detailed list of requirements for this assignment.

https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Programmed-Graphics
for general information on using list comprehensions to generate graphics.

http://brythonserver.github.io/ggame/
for detailed information on ggame.
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
from math import sin,cos,radians

blue=Color(0x0000ff, 1.0)
red=Color(0xff0000, 1.0)
purple=Color(0xff00ff, 1.0)
black=Color(0x000000, 1.0)
tline=LineStyle(1, black)

bc=(CircleAsset(10, tline, blue))
rc=(CircleAsset(10, tline, red))
pc=(CircleAsset(10, tline, purple))

x=0
for i in range(0,36):
    x=int(x+10)
    y=int(100+100*sin(radians(x)))
    c=int(100+100*cos(radians(x)))
    a=int(100+100*cos(radians(x)))
    b=int(400+100*sin(radians(x)))
    Sprite(bc,(x,y))
    Sprite(rc,(x,c))
    Sprite(pc,(a,b))

myapp = App()
myapp.run()