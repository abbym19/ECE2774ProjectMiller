import numpy as np
from Bus import Bus
from Transformer import Transformer
from Bundling import Bundling
from ConductorData import ConductorData
from Geometry import Geometry
from TransmissionLine import TransmissionLine

# Create buses

bus1 = Bus(name="Bus1", base_kv=20)
bus2 = Bus(name="Bus2", base_kv=230)
bus3 = Bus(name="Bus3", base_kv=None)
bus4 = Bus(name="Bus4", base_kv=None)
bus5 = Bus(name="Bus5", base_kv=None)
bus6 = Bus(name="Bus6", base_kv=230)
bus7 = Bus(name="Bus7", base_kv=18)

# Create conductors

# Create ConductorData
conductor_1 = ConductorData(name="Conductor1", gmr=0.0217, sub_resistance=0.385, diameter=0.1013)

# Create bundling

bundling_1 = Bundling(name="Bundling1", num_conductors=2, spacing=1.5, conductor_data=conductor_1)

# Create Geometry

geometry_1 = Geometry(name="Geometry1", spacing=[0, 0, 1, 0, 1, 1])

# Create Transformers

transformer_1 = Transformer(name="Transformer1", power_rating=125, z_percent=0.085, voltage_ratio=10, winding=None,
                            from_bus=bus1, to_bus=bus2)

transformer_2 = Transformer(name="Transformer2", power_rating=200, z_percent=0.105, voltage_ratio=12, winding=None,
                            from_bus=bus6, to_bus=bus7)

# Create Transmission Line
t_1 = TransmissionLine(name="Line1", line_length=10, from_bus=bus2, to_bus=bus4,
                       conductor_data=conductor_1, conductor_geometry=geometry_1,
                       bundling=bundling_1)
t_2 = TransmissionLine(name="Line2", line_length=25, from_bus=bus2, to_bus=bus3,
                       conductor_data=conductor_1, conductor_geometry=geometry_1,
                       bundling=bundling_1)
t_3 = TransmissionLine(name="Line3", line_length=20, from_bus=bus3, to_bus=bus5,
                       conductor_data=conductor_1, conductor_geometry=geometry_1,
                       bundling=bundling_1)
t_4 = TransmissionLine(name="Line4", line_length=20, from_bus=bus4, to_bus=bus6,
                       conductor_data=conductor_1, conductor_geometry=geometry_1,
                       bundling=bundling_1)
t_5 = TransmissionLine(name="Line5", line_length=10, from_bus=bus6, to_bus=bus5,
                       conductor_data=conductor_1, conductor_geometry=geometry_1,
                       bundling=bundling_1)
t_6 = TransmissionLine(name="Line6", line_length=35, from_bus=bus4, to_bus=bus5,
                       conductor_data=conductor_1, conductor_geometry=geometry_1,
                       bundling=bundling_1)


# Initialize Ybus matrix

num_buses = Bus.counter
print(num_buses)
Ybus = np.zeros((num_buses, num_buses), dtype=complex)