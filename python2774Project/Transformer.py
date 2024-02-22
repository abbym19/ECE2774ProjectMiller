import pandas as pd
import numpy as np


class Transformer:

    def __init__(self, voltage_rating_low, voltage_rating_high, power_rating, z_percent, voltage_ratio, winding_config, from_bus, to_bus, S):
        self.name = self
        self.voltage_rating_low = voltage_rating_low
        self.voltage_rating_high = voltage_rating_high
        self.power_rating = power_rating
        self.z_percent = z_percent
        self.voltage_ratio = voltage_ratio
        self.winding_config = winding_config
        self.from_bus = from_bus
        self.to_bus = to_bus
        self.S = S
        self.calculate_zpu()

    def calculate_zpu(self):
        z_pu_magnitude = (self.z_percent/100) * self.S.s_mva / self.power_rating
        z_pu_angle = np.tan(self.voltage_ratio) * self.S.s_mva / self.power_rating
        z_pu = z_pu_magnitude * np.cos(z_pu_angle) + 1j * z_pu_magnitude * np.sin(z_pu_angle)

        return z_pu

