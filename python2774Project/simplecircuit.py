import numpy as np

#define variables for Vs, Rline, Pload, and Vload
Vs = 100
Rline = 5
Pload = 2000
Vload = 100

#calculate Rload
Rload = Vload * Vload / Pload
print('Rload = ')
print(Rload)

#solving for the current
Iline = Vs / (Rline + Rload)
print('\nIline = ')
print(Iline)

#solving for power in the line
Pline = Vs * Vs / (Rline + Rload)
print('\nPline = ')
print(Pline)
