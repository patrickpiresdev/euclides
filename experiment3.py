# experiment 3 - `Line` with translation, rotation and scaling

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from primitives import Line
from transformations import Scale

line = Line(color='black')

fig, ax = plt.subplots()

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

line.transform(Scale(x=2))

line.draw(ax)

plt.show()
