import numpy as np


class Geometry:

    def __init__(self, ab, bc, ac, d):
        self.ab = ab
        self.bc = bc
        self.ac = ac
        self.d = d

    def calculated_eq(self):
        d_eq = np.cbrt(self.ab * self.bc * self.ac)
        return d_eq
