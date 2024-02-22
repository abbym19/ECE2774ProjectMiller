import numpy as np
import Settings as s


class TransmissionLine:

    def __init__(self, name, line_length, from_bus, to_bus, conductor_data, conductor_geometry):
        self.name = name
        self.line_length = line_length
        self.from_bus = from_bus
        self.to_bus = to_bus
        self.conductor_data = conductor_data
        self.conductor_geometry = conductor_geometry
        self.calculate_series_impedance()
        self.calculate_line_resistance()
        self.calculate_line_reactance()

    def calculate_series_impedance(self):
        series_impedance = self.conductor_data.calculate_resistance() + 1j * self.conductor_data.calculate_reactance()

        return series_impedance

    def calculate_line_resistance(self):
        line_resistance = self.conductor_data.calculate_resistance_per_mile * self.line_length

        return line_resistance

    def calculate_line_reactance(self):
        line_reactance = self.conductor_data.calculate_reactance_per_mile * self.line_length

        return line_reactance

    def calculate_shunt_susceptance(self):
        shunt_susceptance = self.conductor_data.calculate_susceptance_per_mile() * self.line_length

