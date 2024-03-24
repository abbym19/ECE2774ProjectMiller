import numpy as np
import Settings as s


class ConductorData:

    def __init__(self, name: str, gmr: float, sub_resistance: float, diameter: float):
        self.name = name
        self.gmr = gmr
        self.sub_resistance = sub_resistance
        self.diameter = diameter


