import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from primitives import Square, Line
from transformations import Scale, Perspective, Rotation, Translation

fig, ax = plt.subplots()

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

square = Square(color='black')

m = 5

# square.transform(Perspective(x=-0.1))

s = 4
# square.transform(Scale(x=s, y=s))

""" step = square.size() / m
lines = []

start = square.size() / 2
for i in range(1, m):
    line = Line(width=1, color='black')
    line.transform(Rotation(angle=90))
    line.transform(Translation(x=-start + i*step))
    line.transform(Scale(y=s))
    lines.append(line)
 """

square.draw(ax)

""" for line in lines:
    line.draw(ax) """

plt.show()
# plt.savefig('test.png', dpi=300)