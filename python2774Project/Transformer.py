import pandas as pd
import numpy as np
import Settings as s


class Transformer:

    def __init__(self, name, power_rating, z_percent, voltage_ratio, winding, from_bus, to_bus):
        self.name = name
        self.power_rating = power_rating
        self.z_percent = z_percent
        self.voltage_ratio = voltage_ratio
        self.winding = winding
        self.from_bus = from_bus
        self.to_bus = to_bus
        self.calculate_zpu()

    def calculate_zpu(self):
        z_pu_magnitude = self.z_percent * s.s_mva / self.power_rating
        z_pu_angle = np.tan(self.voltage_ratio) * s.s_mva / self.power_rating
        z_pu = z_pu_magnitude * np.cos(z_pu_angle) + 1j * z_pu_magnitude * np.sin(z_pu_angle)

        return z_pu

