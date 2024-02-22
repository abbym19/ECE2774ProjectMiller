import numpy as np


class Ybus:

    def __init__(self, n, buses, transmission_line):
        self.n = n
        self.buses = buses
        self.transmission_line = transmission_line
        self.calculate_ybus()
        self.calculate_yshunt()
        self.calculate_yseries()


    def calculate_yshunt(self):
        y_shunt = 1j * self.transmission_line.calculate_shunt_susceptance()

        return y_shunt

    def calculate_yseries(self):
        y_series = 1 / (self.transmission_line.calculate_series_impedance())

        return y_series

    def calculate_ybus(self):
        y_bus = np.zeros(self.n,self.n)

        return y_bus
