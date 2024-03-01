import numpy as np
from ConductorData import ConductorData


class Bundling:
    def __init__(self, name, num_conductors, spacing, conductor_data: ConductorData):
        self.name = name
        self.num_conductors = num_conductors
        self.spacing = spacing
        self.conductor_data = conductor_data
        self.calculated_sl()
        self.calculated_sc()

    def calculated_sl(self):

        if self.num_conductors == 2:
            d_sl = np.sqrt(self.spacing * self.conductor_data.gmr)
        elif self.num_conductors == 3:
            d_sl = np.cbrt(np.power(self.spacing, 2) * self.conductor_data.gmr)
        elif self.num_conductors == 4:
            d_sl = 1.091 * np.power((np.power(self.spacing, 3) * self.conductor_data.gmr), 0.25)

        return d_sl

    def calculated_sc(self):
        if self.num_conductors == 2:
            d_sc = np.sqrt(self.spacing * self.conductor_data.diameter/2)
        elif self.num_conductors == 3:
            d_sc = np.cbrt(np.power(self.spacing, 2) * self.conductor_data.diameter/2)
        elif self.num_conductors == 4:
            d_sc = 1.091 * np.power((np.power(self.spacing, 3) * self.conductor_data.diameter/2), 0.25)

        return d_sc