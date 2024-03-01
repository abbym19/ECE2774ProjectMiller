# transformer class

import numpy as np
import Settings as s
from Bus import Bus


class Transformer:

    def __init__(self, name, power_rating, z_percent, voltage_ratio, winding, from_bus: Bus, to_bus: Bus):

        # Ensure power_rating, z_percent, and voltage_ratio are positive values
        if power_rating <= 0 or z_percent <= 0 or voltage_ratio <= 0:
            raise ValueError("Power rating, z percent, and voltage ratio must be positive values.")

        # Ensure from_bus and to_bus are not the same
        if from_bus == to_bus:
            raise ValueError("From bus and to bus must be different.")

        self.name = name
        self.power_rating = power_rating
        self.z_percent = z_percent
        self.voltage_ratio = voltage_ratio
        self.winding = winding
        self.from_bus = from_bus
        self.to_bus = to_bus
        self.calculate_zpu()
        self.calculate_primitive_admittance_matrix()

    def calculate_zpu(self):
        z_base = np.power(s.v_base, 2) / self.power_rating
        z_pu_magnitude = self.z_percent * s.s_mva / self.power_rating
        z_pu_angle = np.tan(self.voltage_ratio) * s.s_mva / self.power_rating
        z_pu = z_pu_magnitude * np.cos(z_pu_angle) + 1j * z_pu_magnitude * np.sin(z_pu_angle)
        z = z_pu * z_base
        return z

    def calculate_primitive_admittance_matrix(self):

        z_pu = self.calculate_zpu()

        # Calculate primitive admittance matrix
        y_primitive = 1 / z_pu

        # Convert to 2x2 symmetric matrix
        y_primitive_matrix = np.array([[y_primitive, -y_primitive],
                                       [-y_primitive, y_primitive]])

        return y_primitive_matrix

