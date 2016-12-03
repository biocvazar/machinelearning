__author__ = 'Bio'
from locale import atof
import numpy
from matplotlib import pylab as plb
from matplotlib import pyplot as plt
from scipy.signal import butter, findfreqs, lfilter
from scipy import interpolate


def butter_lowpass(wc, order=5):
    b, a = butter(order, wc, btype='low', analog=True)
    return b, a


def butter_lowpass_filter(data, wc, order=5):
    b, a = butter_lowpass(wc, order)
    y = lfilter(b, a, data)
    return y


def sort_v(x:list, y:list):
    icf = 0
    new_y = []
    for i in range(len(x)):
        if (x[i] != x[i - 1]) and i != 0:
            new_y.append(sorted(y[icf:i]))
            icf = i
    new_y.append(sorted(y[icf:]))
    y = []
    for list in new_y:
        y.extend(list)
    return y


count = []
encoder_angle = []
template_angle = []
intensity = []

freq_file = open("v8", "r")

for data in freq_file:
    data = data.split()
    count.append(int(atof(data[0])))
    encoder_angle.append(atof(data[1]))
    template_angle.append(atof(data[2]))
    intensity.append(atof(data[3]))
freq_file.close()

intensity = sort_v(template_angle, intensity)
# print (intensity)

count = numpy.array(count)
encoder_angle = numpy.array(encoder_angle)
template_angle = numpy.array(template_angle)
intensity = numpy.array(intensity)

# print(len(intensity), len(template_angle))

plt.plot(template_angle, intensity, "b-")
plt.autoscale(enable=True, axis='x')
plt.title('intensity/angle')
plt.grid()
plt.show()

const_comp = numpy.sum(intensity) / len(intensity)
order = 2
wc = 0.7

y = butter_lowpass_filter(intensity, wc, order) + const_comp

plt.plot(template_angle, intensity, 'b-', label='data')
plt.plot(template_angle, y, 'g-', linewidth=2, label='filtered data')
plt.ylabel('intensity')
plt.xlabel('angle')
plt.grid()
plt.legend()
plt.show()

print(template_angle[100:500], intensity[100:500])
function = interpolate.interp1d(template_angle, intensity)
# #
new_int = numpy.linspace(template_angle[0], template_angle[-1], num=10**6)
new_angl = function(new_int)
# print(new_angles, new_intensity)

plt.figure()
plt.subplot(221)
plt.title('signal')
plt.plot(template_angle, intensity, 'g.')
plt.subplot(222)
plt.title('linear interpolation')
plt.plot(new_int, new_angl, 'b-')
plt.subplot(212)
plt.title('signal and linear interpolation')
plt.plot(template_angle, intensity, 'g.', new_int, new_angl, 'b-')
plt.show()


def find_zero_interception(x, y, maxx):
    x_zeros = []
    for i in range(len(y) - 1):
        if (y[i] > 0 and y[i + 1] < 0) or (y[i] < 0 and y[i + 1] > 0) or (y[i] == y[i + 1] == 0):
            x1, x2, x3, x4 = 0, maxx, x[i], x[i + 1]
            y1, y2, y3, y4 = 0, 0, y[i], y[i + 1]
            px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / (
                (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
            x_zeros.append(px)
    return x_zeros


template_angle, intensity = template_angle - const_comp, intensity - const_comp
zeros_x = find_zero_interception(template_angle, intensity, max(template_angle))
zeros_y = [0 for _ in range(len(zeros_x))]

plt.plot(template_angle, intensity, 'b-', label="signal")
plt.plot(zeros_x, zeros_y, 'ko', label="zeros")
plt.legend()
plt.show()


amp = max(intensity)/2
larges_i = []
m = []
lrg = []
mn = []
for i in intensity:
    if i > amp:
        larges_i.append(list(numpy.where(intensity == i)[0]))
    if i < -amp:
        m.append(list(numpy.where(intensity == i)[0]))
for l in larges_i:
    lrg.extend(l)
for l in m:
    mn.extend(l)

print(lrg, mn)
tal = numpy.take(template_angle, lrg)
intsl = numpy.take(intensity, lrg)

tam = numpy.take(template_angle, mn)
intsm = numpy.take(intensity, mn)

file = open("max", 'w')
for i in range(len(intsl)):
    file.write(str(tal[i])+" "+str(intsl[i])+"\n")
file.close()
file = open("min", 'w')
for i in range(len(intsm)):
    file.write(str(tam[i])+" "+str(intsm[i])+"\n")
file.close()

intsl2 = numpy.array_split(intsl, 10)
lst = []
for l in intsl2:
     lst.append(list(numpy.where(intensity == max(l))[0]))
maxs = []
for l in lst:
    maxs.extend(l)
talm = numpy.take(template_angle, maxs)
intslm = numpy.take(intensity, maxs)

intsm2 = numpy.array_split(intsm, 10)
lst = []
for l in intsm2:
     lst.append(list(numpy.where(intensity == min(l))[0]))
mins = []
for l in lst:
    mins.extend(l)
tamm = numpy.take(template_angle, mins)
intsmm = numpy.take(intensity, mins)

plt.plot(template_angle, intensity, 'g-', label="signal" )
plt.plot(tal, intsl, 'ro', label="local maxes" )
plt.plot(tam, intsm, 'bo', label="local mines" )
plt.plot(talm, intslm, 'yo', label="maxes" )
plt.plot(tamm, intsmm, 'mo', label="mines")
plt.legend()
plt.show()

maxx = len(talm)
loc_max = len(tal)
minn = len(tamm)
loc_min = len(tam)

plt.figure(2)
plt.subplot(211)
plt.title("Max")
plt.pie((maxx, loc_max), autopct='%1.1f%%', labels=('max', "local max"), colors=('gold', 'lightskyblue'))
plt.subplot(212)
plt.title("Min")
plt.pie((minn, loc_min), autopct='%1.1f%%', labels=('min', "local min"), colors=('gold', 'lightskyblue'))
plt.show()

W = 32 # num points in moving average
xf = numpy.zeros(len(intensity)-W+1)
for i in range(len(intensity)-W+1):
    xf[i] = numpy.mean(intensity[i:i+W])
xf = lfilter(numpy.ones(W)/W, 1, intensity)

plt.figure()
plt.subplot(221)
plt.title('filter 1')
plt.plot(template_angle, y, 'b-', linewidth=2, label='filtered data')
plt.subplot(222)
plt.title('filter 2')
plt.plot(template_angle, xf, 'r-')
plt.subplot(212)
plt.title('signal and filters')
plt.plot(template_angle, intensity, "g-", template_angle, xf, 'r-', template_angle, y-const_comp, 'b-')
plt.show()


if1 = numpy.array_split(y, 10)
lst = []
for l in if1:
     lst.append(list(numpy.where(y == max(l))[0]))
maxsf1 = []
for l in lst:
    maxsf1.extend(l)

if2 = numpy.array_split(xf, 10)
lst = []
for l in if2:
     lst.append(list(numpy.where(xf == max(l))[0]))
maxsf2 = []
for l in lst:
    maxsf2.extend(l)

plt.title("Maxes")
plt.pie((maxx, len(maxsf1), len(maxsf2)), autopct='%1.1f%%', labels=('signal', 'filter1', "filter2"), colors=('gold', 'lightskyblue', 'magenta'))
plt.show()