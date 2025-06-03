# experiment 2 - perspective

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from transformations import Translation, Perspective

import numpy as np

fig, ax = plt.subplots()

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

line1 = np.array([(-1, -4, 0, 1), (-1, 4, 0, 1)]).T
line2 = np.array([(1, -4, 0, 1), (1, 4, 0, 1)]).T

translation = Translation(y=2)
line1 = translation.apply(line1)
line2 = translation.apply(line2)

perspective = Perspective(y=0.4)
line1 = perspective.apply(line1)
line2 = perspective.apply(line2)

ax.plot(line1[0], line1[1])
ax.plot(line2[0], line2[1])

plt.show()
