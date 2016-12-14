__author__ = 'Bio'

import numpy
import matplotlib.pyplot as plt
data = []

file = open('town.txt', 'r', encoding='utf-8')
for t in file:
    d = t.split()
    print(d)
    if d[5] == "Львівська":
        d[0] = int(d[0])
        d[1] = float(d[1])
        d[2] = int(d[2])
        d[3] = int(d[3])
        d[4] = int(d[4])
        data.append(d)
file.close()

print(data)
X = []
Y = []
for d in data:
    money, customers, year, investment, employee = d[0], d[1], d[2], d[3], d[4]
    x = investment / customers
    y = ((2016 - year) * money) / employee
    X.append(x)
    Y.append(y)

# X = numpy.array(X)
# Y = numpy.array(Y)

X2 = list(map(lambda x: x*x, X))
Y2 = list(map(lambda y: y*y, Y))
XY = list(map(lambda x, y: x*y, X, Y))

sumX = sum(X)
sumX2 = sum(X2)
sumY = sum(Y)
sumXY = sum(XY)
print(sumX ,
sumX2,
sumY ,
sumXY)
a = numpy.array([[sumX2, sumX], [sumX, len(X)]])
b = numpy.array([sumXY, sumY])

z = numpy.linalg.solve(a, b)
# print(X2, Y2, XY)


linY = []
for i in range(len(X)):
    x = X[i] * z[0] + z[1]
    linY.append(x)

v_customers = 90
v_investment = 250
v_x = v_customers/v_investment
v_y = v_x * z[0] + z[1]

fig = plt.figure()
ax = fig.add_subplot(111)
plt.title('LinRegr')
plt.xlabel('investments/customers')
plt.ylabel('money/employee')
ax.plot(X, Y, 'ro')
ax.plot(X, linY, 'b-')
ax.plot(v_x, v_y, 'yo')
indx = [1, 7, 8, 12, 15]
for i in range(len(X)):
    ax.annotate('M%d' % indx[i], xy=(X[i], Y[i]), textcoords='data')
ax.annotate('V8', xy=(v_x, v_y), textcoords='data')
plt.show()

