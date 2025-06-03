# experiment 1 - `Dot` with translation and rotation
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from primitives import Dot
from transformations import Translation, Rotation, Perspective

fig, ax = plt.subplots()

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

d1 = Dot(0, 0, 0, color='black', marker='o', size=9)

d2 = d1.copy()
d2.set_color('red')

d2.transform(Translation(x=2))
d2.transform(Rotation(angle=90, y=True))

perspective = Perspective(x=0, y=0, z=0)
d1.transform(perspective)
d2.transform(perspective)

d1.draw(ax)
d2.draw(ax)

plt.show()
