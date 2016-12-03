from locale import atoi
from math import factorial
import pylab

__author__ = 'Bio'

import matplotlib.pyplot as plt
import matplotlib.pylab
import matplotlib.image as mpimg
import numpy as np


class LineBuilder:
    def __init__(self, line):
        self.line = line
        self.xs = list(line.get_xdata())
        self.ys = list(line.get_ydata())
        self.length = 0

        self.x = []
        self.y = []
        self.beze_points = []

    def search_length(self):
        length_x = 0
        length_y = 0
        for i in range(len(self.xs) - 1):
            length_x += abs(self.xs[i + 1] - self.xs[i])
            length_y += abs(self.ys[i + 1] - self.ys[i])
        self.length = int(((length_x ** 2 + length_y ** 2) ** 0.5) * 4)
        print(str(self.length) + "m")


    def get_ni(self, n, i):
        return factorial(n) / (factorial(i) * factorial(n - i))


    def get_I(self, t, n, i):
        return self.get_ni(n, i) * (t ** i) * (1 - t) ** (n - i)


    def change_n(self):
        return len(self.xs)


    def sum(self, t):
        n = self.change_n()
        x, y = 0, 0
        for i in range(n):
            x += self.xs[i] * self.get_I(t, n - 1, i)
            y += self.ys[i] * self.get_I(t, n - 1, i)
        self.x.append(x)
        self.y.append(y)

    def calculate_Beze(self):
        t = 0
        c = 0
        while t <= 1:
            self.beze_points.append(self.sum(t))
            t += 0.01
            c += 1


def convertx(stops):
    x = []
    for stop in stops:
        x.append(stop[0])
    return x


def converty(stops):
    y = []
    for stop in stops:
        y.append(stop[1])
    return y


def onclick(event):
    if event.xdata != None and event.ydata != None:
        pass


def onpick(event):
    thisline = event.artist
    xdata = thisline.get_xdata()
    ydata = thisline.get_ydata()
    ind = event.ind
    points = tuple(zip(xdata[ind], ydata[ind]))
    # print('onpick points:', points)
    linebuilder.xs.append(points[0][0])
    linebuilder.ys.append(points[0][1])
    linebuilder.line.set_data(linebuilder.xs, linebuilder.ys)
    linebuilder.search_length()
    ax.set_title('Map (' + str(linebuilder.length) + "m)")

    linebuilder_b.x.clear()
    linebuilder_b.y.clear()
    linebuilder_b.xs.append(points[0][0])
    linebuilder_b.ys.append(points[0][1])
    linebuilder_b.calculate_Beze()
    linebuilder_b.line.set_data(linebuilder_b.x, linebuilder_b.y)


    linebuilder.line.figure.canvas.draw()
    linebuilder_b.line.figure.canvas.draw()


def press(event):
    print('press', event.key)
    if event.key == ' ':
        line, = ax.plot([], [], 'gold', lw=3)
        linebuilder.xs.clear()
        linebuilder.ys.clear()
        linebuilder.length = 0
        linebuilder.line.figure.canvas.draw()
        linebuilder_b.xs.clear()
        linebuilder_b.ys.clear()
        linebuilder_b.length = 0
        linebuilder_b.line.figure.canvas.draw()


fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111)
ax.set_title('Map')
img = mpimg.imread("map.png")
imgplot = plt.imshow(img)
plt.axis('off')


cid = fig.canvas.mpl_connect('button_press_event', onclick)
fig.canvas.mpl_connect('pick_event', onpick)
fig.canvas.mpl_connect('key_press_event', press)

tstops = []
bstops = []
tmstops = []
with open("stops") as stops:
    for row in stops:
        stop = row.split()
        if stop[2] == 'r':
            tstops.append((atoi(stop[0]), atoi(stop[1])))
        if stop[2] == 'b':
            bstops.append((atoi(stop[0]), atoi(stop[1])))
        if stop[2] == 'y':
            tmstops.append((atoi(stop[0]), atoi(stop[1])))

plt.plot(convertx(tstops), converty(tstops), 'ro--', picker=5, label="Trum stop")
plt.plot(convertx(bstops), converty(bstops), 'b*--', picker=5, label="Bus stop")
plt.plot(convertx(tmstops), converty(tmstops), 'ys--', picker=5, label="Trolley stop")

line, = ax.plot([], [], 'gold', lw=3, label="Path")
linebuilder = LineBuilder(line)
line2, = ax.plot([], [], 'k-.', lw=2, label="Interpolated path")
linebuilder_b = LineBuilder(line2)
pylab.legend(loc="upper right",)

plt.show()