import numpy as np
import Settings as s


class ConductorData:

    def __init__(self, name, gmr, sub_resistance, diameter):
        self.name = name
        self.gmr = gmr
        self.sub_resistance = sub_resistance
        self.diameter = diameter


