from Circuit import Circuit

# add circuit class

seven_bus = Circuit('7 Bus System')
seven_bus.add_bus_element("bus 1", 20)
seven_bus.add_bus_element("bus 2", 230)
seven_bus.add_bus_element("bus 3", 230)
seven_bus.add_bus_element("bus 4", 230)
seven_bus.add_bus_element("bus 5", 230)
seven_bus.add_bus_element("bus 6", 230)
seven_bus.add_bus_element("bus 7", 18)

seven_bus.add_transformer_element("T1", 125, 8.5, 10, "bus 1", "bus 2")


# Create ConductorData
seven_bus.add_conductor_element(name="Conductor1", gmr=0.0217, sub_resistance=0.385, diameter=0.1013)

# Create bundling
seven_bus.add_bundling_element(name="Bundling1", num_conductors=2, spacing=1.5, conductor_data="Conductor1")

# Create Geometry

seven_bus.add_geometry_element(name="Geometry1", spacing=[9.75, 0, 19.5, 0, 29.25, 0])


# Create Transmission Line
seven_bus.add_tline_element(name="Line1", line_length=10, bus1="bus 2", bus2="bus 4",
                            conductor_data="Conductor1", conductor_geometry="Geometry1",
                            bundling="Bundling1")
seven_bus.add_tline_element(name="Line2", line_length=25, bus1="bus 2", bus2="bus 3",
                            conductor_data="Conductor1", conductor_geometry="Geometry1",
                            bundling="Bundling1")
seven_bus.add_tline_element(name="Line3", line_length=20, bus1="bus 3", bus2="bus 5",
                            conductor_data="Conductor1", conductor_geometry="Geometry1",
                            bundling="Bundling1")
seven_bus.add_tline_element(name="Line4", line_length=20, bus1="bus 4", bus2="bus 6",
                            conductor_data="Conductor1", conductor_geometry="Geometry1",
                            bundling="Bundling1")
seven_bus.add_tline_element(name="Line5", line_length=10, bus1="bus 6", bus2="bus 5",
                            conductor_data="Conductor1", conductor_geometry="Geometry1",
                            bundling="Bundling1")
seven_bus.add_tline_element(name="Line6", line_length=35, bus1="bus 4", bus2="bus 5",
                            conductor_data="Conductor1", conductor_geometry="Geometry1",
                            bundling="Bundling1")

