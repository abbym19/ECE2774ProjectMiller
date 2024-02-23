import numpy as np
import Settings as s


class TransmissionLine:

    def __init__(self, name, line_length, from_bus, to_bus, conductor_data, conductor_geometry, bundling):
        self.name = name
        self.line_length = line_length
        self.from_bus = from_bus
        self.to_bus = to_bus
        self.conductor_data = conductor_data
        self.conductor_geometry = conductor_geometry
        self.bundling = bundling
        self.calculate_resistance()
        self.calculate_reactance()
        self.calculate_susceptance()
        self.calculate_series_impedance()

    def calculate_resistance(self):
        phase_resistance = self.conductor_data.sub_resistance / self.bundling.num_conductors * self.line_length

        return phase_resistance

    def calculate_reactance(self):
        ln = self.conductor_geometry.calculated_eq() / self.bundling.calculated_sl()
        x_p = 2 * np.pi * s.f * 2 * np.exp(-7) * np.log(ln) * 1609

        return x_p

    def calculate_susceptance(self):
        ln = self.conductor_geometry.calculated_eq() / self.bundling.calculated_sc()
        b_p = 2 * np.pi * s.f * 2 * np.pi * 8.854e-12 / np.log(ln) * 1609 * self.line_length

        return b_p

    def calculate_series_impedance(self):
        series_impedance = self.calculate_resistance() + 1j * self.calculate_reactance()

        return series_impedance


