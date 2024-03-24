from typing import Dict, List, Optional
from Bus import Bus
from Transformer import Transformer
from Bundling import Bundling
from ConductorData import ConductorData
from Geometry import Geometry
from TransmissionLine import TransmissionLine


class Circuit:
    def __init__(self, name: str):

        self.name: str = name

        self.bus_order: List[str] = list()
        self.buses: Dict[str, Bus] = dict()
        self.transformers: Dict[str, Transformer] = dict()
        self.bundles: Dict[str, Bundling] = dict()
        self.conductors: Dict[str,ConductorData] = dict()
        self.geometry: Dict[str, Geometry] = dict()
        self.t_lines: Dict[str, TransmissionLine] = dict()

    def add_bus_element(self, name, base_kv):
        self.buses[name] = Bus(name, base_kv)

    def add_transformer_element(self, name: str, power_rating: float, z_percent: float, voltage_ratio: float, bus1: str, bus2: str):
        self.transformers[name] = Transformer(name, power_rating, z_percent, voltage_ratio, self.buses[bus1], self.buses[bus2])

    def add_bundling_element(self, name: str, num_conductors: float, spacing: float, conductor_data: str):
        self.bundles[name] = Bundling(name, num_conductors, spacing, self.conductors[conductor_data])

    def add_conductor_element(self, name: str, gmr: float, sub_resistance: float, diameter: float):
        self.conductors[name] = ConductorData(name, gmr, sub_resistance, diameter)

    def add_geometry_element(self, name: str, spacing):
        self.geometry[name] = Geometry(name, spacing)

    def add_tline_element(self, name: str, line_length: float, bus1: str, bus2: str, conductor_data: str,
                          conductor_geometry: str, bundling: str):
        self.t_lines[name] = TransmissionLine(name, line_length, self.buses[bus1], self.buses[bus2],
                                              self.conductors[conductor_data], self.geometry[conductor_geometry],
                                              self.bundles[bundling])
