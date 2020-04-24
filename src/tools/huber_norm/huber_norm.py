#!/bin/python

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(-4.0, 4.0, 0.01)
s = []
delta = 1.0

for t1 in t:
    if abs(t1) <= delta:
        L_delta = t1*t1/2.0
    else:
        L_delta = (abs(t1) - delta/2.0) # delta*(abs(t1) - delta/2.0)

    s.append(L_delta)

print t
print s

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='x (s)', ylabel='Huber Loss (delta=' + str(delta) + ')',
       title='Huber Loss')
ax.grid()
plt.show()