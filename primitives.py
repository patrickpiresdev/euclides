import numpy as np
from matplotlib.patches import PathPatch
from matplotlib.path import Path
from transformations import Transformation

class Dot:
    # todo: maybe the dot class is unnecessary and can be done with a circle when there is one
    def __init__(self, x, y, z, marker='.', size=2, color='white', edge_color='none'):
        self.position = np.array((x, y, z, 1)).T
        self.color = color
        self.size = size
        self.marker = marker
        self.edge_color = edge_color

    def draw(self, ax):
        x = self.position[0]
        y = self.position[1]

        marker_style = dict(marker=self.marker, markersize=self.size, color=self.color, markeredgecolor=self.edge_color)

        ax.plot(x, y, **marker_style)

    def transform(self, transformation):
        self.position = transformation.apply(self.position).matrix
    
    def copy(self):
        c = Dot(*self.position[:3])
        c.color = self.color
        c.size = self.size
        c.marker = self.marker
        c.edge_color = self.edge_color
        return c
    
    def set_color(self, c):
        self.color = c


class Line:
    def __init__(self, size=1, width=2, color='white', points=None):
        if points:
            self.points = np.array(points).T
        else:
            half = size / 2
            self.points = np.array([(-half, 0, 0, 1), (half, 0, 0, 1)]).T

        self.width = width
        self.color = color

    def draw(self, ax):
        xs = self.points[0]
        ys = self.points[1]

        ax.plot(xs, ys, color=self.color, linewidth=self.width)

    def transform(self, transformation):
        self.points = transformation.apply(self.points)

    def __str__(self):
        return self.points


class Triangle:
    def __init__(self, base=1, height=1, color='white'):
        self.lines = []
        self.color = color
        
        base_half = base / 2
        height_half = height / 2

        p1 = (0, height_half, 0, 1)
        p2 = (-base_half, -height_half, 0, 1)
        p3 = (base_half, -height_half, 0, 1)
        
        self.points = np.array([p1, p2, p3]).T

    def draw(self, ax):
        ps = np.append(self.points.T, [self.points.T[0]], axis=0).T
        ax.plot(ps[0], ps[1], color=self.color)

    def transform(self, transformation):
        self.points = transformation.apply(self.points)
    
    def __str__(self):
        return self.lines.__str__()

class Square:
    def __init__(self, size=1, color='white'):
        half = size / 2
        self.points = np.array([
            ( half,  half, 0, 1),
            (-half,  half, 0, 1),
            (-half, -half, 0, 1),
            ( half, -half, 0, 1)
        ]).transpose()
        self.color = color
        self.T = Transformation(np.identity(4))
    
    def size(self):
        return abs(self.points[0][0] - self.points[0][1])

    def draw(self, ax):
        points = self.T.apply(self.points).matrix

        codes = [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
        vertices = []
        for i in range(4):
            vertices.append((points[0][i], points[1][i]))
        vertices.append((0, 0))
        path = Path(vertices, codes)
        pathpatch = PathPatch(path, facecolor='none', edgecolor=self.color)
        ax.add_patch(pathpatch)

    def transform(self, transformation):
        self.T = transformation.apply(self.T.matrix)

class Grid:
    def __init__(self, n=0, m=0, color='white', linewidth=1):
        self.n = n
        self.m = m
        self.color = color
        self.linewidth = linewidth