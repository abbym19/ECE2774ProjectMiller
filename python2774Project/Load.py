import pandas as pd
import numpy as np
import Settings as s

class Load:

    def __init__(self, name, bus1, p, v):
        self.name = name
        self.bus1 = bus1
        self.p = p
        self.v = v

        self.r = v ** 2 / p

        self.buses = [self.bus1]

    def calc_g(self):
        g = 1 / self.r
        g_df = pd.DataFrame()

        g_df.loc[self.bus1, self.bus1] = g

        self.g = g_df