from math import cos, sin, atan, pi


def Pol2Dec(pol_point):
    r, fi = pol_point
    x = r * cos(fi)
    y = r * sin(fi)
    return x, y


def Dec2Pol(dec_point):
    x, y = dec_point
    r = (x ** 2 + y ** 2) ** 0.5
    if x > 0 and y >= 0:
        fi = atan(y / x)
        return r, fi
    elif x > 0 and y < 0:
        fi = atan(y / x) + 2 * pi
        return r, fi
    elif x < 0:
        fi = atan(y / x) + pi
        return r, fi
    elif x == 0 and y > 0:
        fi = pi / 2
        return r, fi
    elif x == 0 and y < 0:
        fi = 3 * pi / 2
        return r, fi


if __name__ == "__main__":
    print(Dec2Pol((3, 4)))
    print(Pol2Dec((5.0, 0.9272952180016122)))