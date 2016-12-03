__author__ = 'Bio'

from graphics import *

def draw_rectangle(coordinate:list, a:int, b:int, color:str, window):
    x, y = coordinate
    vertices = [Point(x, y), Point(a + x, y), Point(a + x, b + y), Point(x, b + y)]
    poly = Polygon(vertices)
    poly.setFill(color)
    poly.draw(window)

# 1.1
# win = GraphWin("lab 1. 1", 400, 400)
# x, y = 100, 100
# a = 100
# draw_rectangle([x, y], a, a, "blue", win)
# draw_rectangle([x+a, y+a], a, a, "blue", win)
# draw_rectangle([x+a, y], a, a, "red", win)
# draw_rectangle([x, y+a], a, a, "red", win)
#
# draw_rectangle([x+a+a/4, y+a/4], a/2, a/2, "blue", win)
# draw_rectangle([x+a/4, y+a+a/4], a/2, a/2, "blue", win)
# draw_rectangle([x+a/4, y+a/4], a/2, a/2, "red", win)
# draw_rectangle([x+a+a/4, y+a+a/4], a/2, a/2, "red", win)
# win.getMouse()
# win.close()


#1.2
# win = GraphWin("lab 1.2", 400, 400)
#
# x, y = 100, 100
# a = ((8*2**0.5)**2)/2
# for i in range(3):
#         draw_rectangle([x+i*a, y], a, a, "green", win)
#         draw_rectangle([x+i*a, y+a], a, a, "white", win)
#
# win.getMouse()
# win.close()

#2.1

def new_coordinate(zero:Point, point:Point):
    x = point.getX() - zero.getX()
    y = point.getY() - zero.getY()
    return x, y

win = GraphWin("lab 2.1", 200, 200)
zero = Point(win.width/2, win.height/2)
cir = Circle(Point(win.width/2, win.height/2), 25)
cir.setOutline('red')
cir.setFill('red')
cir.draw(win)
for i in range(5):
    point = win.getMouse()
    x, y = new_coordinate(zero, point)
    zero = point
    cir.move(x, y)

win.getMouse()
win.close()