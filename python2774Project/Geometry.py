import numpy as np

# array will look like [x1, y1, x2, y2, x3, y3]


class Geometry:

    def __init__(self, name: str, spacing):
        self.name = name
        self.spacing = spacing
        self.calculate_ab()
        self.calculate_bc()
        self.calculate_ac()

    def calculate_ab(self):
        ab = np.sqrt(np.power(self.spacing[2] - self.spacing[0],2)+np.power(self.spacing[3] - self.spacing[1], 2))

        return ab

    def calculate_bc(self):
        bc = np.sqrt(np.power(self.spacing[4] - self.spacing[2],2)+np.power(self.spacing[5] - self.spacing[3], 2))

        return bc

    def calculate_ac(self):
        ac = np.sqrt(np.power(self.spacing[5] - self.spacing[1],2)+np.power(self.spacing[4] - self.spacing[0], 2))

        return ac

    def calculated_eq(self):
        d_eq = np.cbrt(self.calculate_ab() * self.calculate_bc() * self.calculate_ac())
        return d_eq
