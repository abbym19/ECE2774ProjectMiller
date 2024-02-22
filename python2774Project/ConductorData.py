import numpy as np


class ConductorData:

    def __init__(self, num_conductors, gmr, radius, subcond_resistance, conductor_geometry, setting):
        self.num_conductors = num_conductors
        self.gmr = gmr
        self.radius = radius
        self.setting = setting
        self.subcond_resistance = subcond_resistance
        self.conductor_geometry = conductor_geometry
        self.calculated_sl()
        self.calculated_sc()
        self.calculate_resistance_per_mile()
        self.calculate_reactance_per_mile()
        self.calculate_susceptance_per_mile()

    def calculated_sl(self):

        if self.num_conductors == 2:
            d_sl = np.sqrt(self.conductor_geometry.d * self.gmr)
        if self.num_conductors == 3:
            d_sl = np.cbrt(np.power(self.conductor_geometry.d, 2)* self.gmr)
        if self.num_conductors == 4:
            d_sl = 1.091 * np.power((np.power(self.conductor_geometry.d, 3)* self.gmr), 0.25)

        return d_sl

    def calculated_sc(self):
        if self.num_conductors == 2:
            d_sc = np.sqrt(self.conductor_geometry.d * self.radius)
        if self.num_conductors == 3:
            d_sc = np.cbrt(np.power(self.conductor_geometry.d, 2)* self.radius)
        if self.num_conductors == 4:
            d_sc = 1.091 * np.power((np.power(self.conductor_geometry.d, 3) * self.radius), 0.25)

        return d_sc

    def calculate_resistance_per_mile(self):
        phase_resistance = self.subcond_resistance / self.num_conductors

        return phase_resistance

    def calculate_reactance_per_mile(self):
        ln = self.conductor_geometry.calculated_eq / self.calculated_sl()
        x_p = 2 * np.pi * self.setting.f * 2 * np.exp(-7) * np.log(ln) * 1609

        return x_p

    def calculate_susceptance_per_mile(self):
        ln = self.conductor_geometry.calculated_eq / self.calculated_sc
        b_p = 2 * np.pi * self.setting.f * 2 * np.pi * 8.854e-12 / np.log(ln) * 1609

        return b_p

