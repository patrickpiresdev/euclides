# experiment 4 - `Triangle` with translation, rotation and scaling

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from primitives import Triangle
from transformations import Translation, Scale

fig, ax = plt.subplots()

plt.style.use('dark_background')

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

triangle = Triangle(color='black')

s = 100
triangle.transform(Scale(x=s, y=s))
triangle.transform(Translation(y=-s/2))
triangle.draw(ax)

plt.show()