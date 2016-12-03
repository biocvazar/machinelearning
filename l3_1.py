__author__ = 'Bio'

from math import *
import matplotlib.pyplot as plt

file = open("freq_data", "w")
r = [1 * 10 ** 9, 7 * 10 ** 9]
step = 2 * 10 ** 8
I = []
F = []
for f in range(r[0], r[1], step):
    F.append(f)
    I.append(sin(radians(2 * pi * f)))
    file.write(str(f) + " " + str(I[-1]) + '\n')
file.close()

file = open("freq_data", "r")
print("f \t i")
for row in file:
    lst = row.split(' ')
    print(str(lst[0]) + " \t " + str(lst[1]))
file.close()
mx = [F[I.index(max(I))], max(I)]
mn = [F[I.index(min(I))], min(I)]

plt.plot(F, I, 'b', lw=2)
plt.plot(mx[0], mx[1], 'ro')
plt.plot(mn[0], mn[1], 'ro')
plt.annotate('max', xy=mx)
plt.annotate('min', xy=mn)
zeros = [[f, i] for f, i in zip(F, I) if (f == 0 and i == 0)]
try:
    plt.plot(zeros[0][0], zeros[0][1], 'gs')
    plt.annotate('zero', xy=(zeros[0][0], zeros[0][1]))
except Exception:
    pass

plt.show()
Ipidiv2 = []
for f in range(r[0], r[1], step):
    Ipidiv2.append(sin(radians(2 * pi * f + pi / 2)))

plt.plot(F, I, 'g-')
plt.plot(F, Ipidiv2, 'r--')
plt.show()

plt.figure(3)
plt.subplot(311)
plt.title('normal')
plt.plot(F, I, 'b')
Ipidiv4 = []
for f in range(r[0], r[1], step):
    Ipidiv4.append(sin(radians(2 * pi * f + pi / 4)))

plt.subplot(312)
plt.title('pi/4')
plt.plot(F, Ipidiv4, 'r')
Ipidiv8 = []
for f in range(r[0], r[1], step):
    Ipidiv8.append(sin(radians(2 * pi * f + pi / 8)))

plt.subplot(313)
plt.title('pi/8')
plt.plot(F, Ipidiv8, 'g')
plt.show()

d1030 = [0, 0]
d3150 = [0, 0]
d5170 = [0, 0]


def count(lst):
    if i > 0:
        lst[0] += 1
    elif i < 0:
        lst[1] += 1


for f in range(r[0], r[1], step):
    i = sin(radians(2 * pi * f))
    if f <= 3 * 10 ** 9:
        count(d1030)
    if 3.1 * 10 ** 9 <= f <= 5 * 10 ** 9:
        count(d3150)
    if 5.1 * 10 ** 9 <= f <= 7 * 10 ** 9:
        count(d5170)

labels = '+', '-'
colors = 'gold', 'lightskyblue'
plt.figure(3)
plt.subplot(311)
plt.title("10-30 HHz")
plt.pie((d1030[0], d1030[1]), autopct='%1.1f%%', labels=labels, colors=colors)
plt.axis('equal')

plt.subplot(312)
plt.title("31-50 HHz")
plt.pie((d3150[0], d3150[1]), autopct='%1.1f%%', labels=labels, colors=colors)
plt.axis('equal')

plt.subplot(313)
plt.title("51-70 HHz")
plt.pie((d5170[0], d5170[1]), autopct='%1.1f%%', labels=labels, colors=colors)
plt.axis('equal')

plt.show()
