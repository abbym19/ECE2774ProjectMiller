import numpy as np
import Settings as s
from ConductorData import ConductorData
from Geometry import Geometry
from Bundling import Bundling
from Bus import Bus


class TransmissionLine:

    def __init__(self, name: str, line_length: float, bus1: Bus, bus2: Bus, conductor_data: ConductorData,
                 conductor_geometry: Geometry, bundling: Bundling):
        self.name = name
        self.line_length = line_length
        self.bus1 = bus1
        self.bus2 = bus2
        self.conductor_data = conductor_data
        self.conductor_geometry = conductor_geometry
        self.bundling = bundling
        self.calculate_resistance()
        self.calculate_reactance()
        self.calculate_susceptance()
        self.calculate_series_impedance()
        self.calculate_primitive_admittance_matrix()
        self.calculate_shunt_admittance()

    def calculate_resistance(self):
        phase_resistance = self.conductor_data.sub_resistance / self.bundling.num_conductors * self.line_length

        return phase_resistance

    def calculate_reactance(self):
        ln = self.conductor_geometry.calculated_eq() / self.bundling.calculated_sl()
        x_p = 2 * np.pi * s.f * 2 * 10 ** -7 * np.log(ln) * 1609 * self.line_length

        return x_p

    def calculate_susceptance(self):
        ln = self.conductor_geometry.calculated_eq() / self.bundling.calculated_sc()
        b_p = 2 * np.pi * s.f * 2 * np.pi * 8.854e-12 / np.log(ln) * 1609 * self.line_length

        return b_p

    def calculate_series_impedance(self):
        series_impedance = self.calculate_resistance() + 1j * self.calculate_reactance()

        return series_impedance

    def calculate_primitive_admittance_matrix(self):
        primitive_admittance_matrix = np.zeros((2, 2), dtype=complex)

        primitive_admittance_matrix[0, 0] = primitive_admittance_matrix[1, 1] = self.calculate_series_impedance() + self.calculate_susceptance() / 2
        primitive_admittance_matrix[0, 1] = primitive_admittance_matrix[1, 0] = -1 * self.calculate_series_impedance()

        return primitive_admittance_matrix

    def calculate_shunt_admittance(self):
        shunt_admittance = 1 / self.calculate_resistance() + 1j * self.calculate_susceptance()

        return shunt_admittance
