import pandas as pd
import numpy as np
import Settings as s

class Bus:

    counter = 0

    def __init__(self, name):
        self.name = name
        self.index = Bus.counter

        self.v = None

        Bus.counter = Bus.counter + 1

    def set_bus_v(self, bus_v):
        self.v = bus_v