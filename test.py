import numpy as np
from pycse import regress
import matplotlib.pyplot as plt
import uncertainties as u
from scipy.optimize import fsolve


T = np.array([x[0] for x in data])
E1 = np.array([x[1] for x in data])
E2 = np.array([x[2] for x in data])

E = E1 - E2

# columns of the x-values for a line: constant, T
A = np.column_stack([T**0, T])

p, pint, se = regress(A, E, alpha=0.05)

b = u.ufloat((p[0], se[0]))
m = u.ufloat((p[1], se[1]))

@u.wrap
def f(b, m):
    X, = fsolve(lambda x: b + m * x, 800)
    return X

print (f(b, m))