import numpy as np

class Transformation:
    def __init__(self, matrix):
        self.matrix = matrix

    def apply(self, points):
        # todo: alterar nome `points`, pois pode ser outra transformacao
        return Transformation(np.dot(self.matrix, points))


class Translation(Transformation):
    def __init__(self, x=0, y=0, z=0):
        self.matrix = np.array([
            [1, 0, 0, x],
            [0, 1, 0, y],
            [0, 0, 1, z],
            [0, 0, 0, 1]
        ])


class Rotation(Transformation):
    def __init__(self, angle, x=False, y=False):
        # angle: angulo em graus
        # rotacao default em relacao a z
        angle_rad = angle*np.pi / 180
        
        if x:
            self.matrix = self.x_rotation(angle_rad)
        elif y:
            self.matrix = self.y_rotation(angle_rad)
        else:
            self.matrix = self.z_rotation(angle_rad)

    
    def x_rotation(self, deg):
        sin = np.sin(deg)
        cos = np.cos(deg)

        return np.array([
            [1,  0 ,   0 , 0],
            [0, cos, -sin, 0],
            [0, sin,  cos, 0],
            [0,  0,    0,  1]
        ])
    
    def y_rotation(self, deg):
        sin = np.sin(deg)
        cos = np.cos(deg)

        return np.array([
            [ cos, 0, sin, 0],
            [  0,  1,  0 , 0],
            [-sin, 0, cos, 0],
            [  0,  0,  0,  1]
        ])
    
    def z_rotation(self, deg):
        sin = np.sin(deg)
        cos = np.cos(deg)

        return np.array([
            [cos, -sin, 0, 0],
            [sin,  cos, 0, 0],
            [0,     0,  1, 0],
            [0,     0,  0, 1]
        ])


class Scale(Transformation):
    def __init__(self, x=1, y=1, z=1):
        self.matrix = np.array([
            [x, 0, 0, 0],
            [0, y, 0, 0],
            [0, 0, z, 0],
            [0, 0, 0, 1]
        ])


class Perspective(Transformation):
    def __init__(self, x=0, y=0, z=0):
        self.matrix = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [x, y, z, 1]
        ])
    
    def apply(self, points):
        ps = super().apply(points).matrix
        last = ps[3]
        # normaliza
        return Transformation(ps / last)