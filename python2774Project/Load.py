import pandas as pd
import numpy as np
import Settings as s


class Load:

    def __init__(self, name, bus1, p, q):
        self.name = name
        self.bus1 = bus1
        self.p = p
        self.q = q
