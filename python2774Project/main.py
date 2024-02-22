import numpy as np

#z01 = 1j * 0.05

Y = np.array([[7.69 - 1j * 38.36, -3.84 + 1j * 19.23, -3.84 + 1j * 19.23],
              [-3.84 + 1j * 19.23, 7.69 - 1j * 38.36, -3.84 + 1j * 19.23],
              [-3.84 + 1j * 19.23, -3.84 + 1j * 19.23, 7.69 - 1j * 38.36]])

v0 = 1.0
ang0 = 0.0

p1 = 2.25
q1 = 0.7
v1 = 1.0
ang1 = 0

v2 = 1.0
ang2 = 0

V = np.array([v0 * np.exp(1j * ang0), v1 * np.exp(1j * ang1), v2 * np.exp(1j * ang2)])

p1_inj = p1
q1_inj = q1

y = np.array([p1_inj, q1_inj])
print("Power injections of PV and PQ buses:\n")
print(f"Bus {1}: P = {y[0]:.4f} Q = {y[1]:.4f}")

x = np.array([ang1, abs(v2), ang2])

max_iterations = 6
tolerance = 1e-8

for iteration in range(max_iterations):

    print(f"\n\n--------Iteration {iteration}---------")

    # Power flow calculations for Bus 0
    p0_calculated = (abs(V[0]) * abs(V[0]) * abs(Y[0, 0]) * np.cos(np.angle(V[0]) - np.angle(V[0]) - np.angle(Y[0, 0])))
    q0_calculated = (abs(V[0]) * abs(V[0]) * abs(Y[0, 0]) * np.sin(np.angle(V[0]) - np.angle(V[0]) - np.angle(Y[0, 0])))

    # Power flow calculations for Bus 1
    p1_calculated = (abs(V[1]) * abs(V[0]) * abs(Y[1, 0]) * np.cos(np.angle(V[1]) - np.angle(V[0]) - np.angle(Y[1, 0]))
                     + abs(V[1]) * abs(V[1]) * abs(Y[1, 1]) * np.cos(np.angle(V[1]) - np.angle(V[1]) - np.angle(Y[1, 1])))
    q1_calculated = (abs(V[1]) * abs(V[0]) * abs(Y[1, 0]) * np.sin(np.angle(V[1]) - np.angle(V[0]) - np.angle(Y[1, 0]))
                     + abs(V[1]) * abs(V[1]) * abs(Y[1, 1]) * np.sin(np.angle(V[1]) - np.angle(V[1]) - np.angle(Y[1, 1])))

    # Power flow calculations for Bus 2
    p2_calculated = (abs(V[2]) * abs(V[0]) * abs(Y[2, 0]) * np.cos(np.angle(V[2]) - np.angle(V[0]) - np.angle(Y[2, 0]))
                     + abs(V[2]) * abs(V[1]) * abs(Y[2, 1]) * np.cos(np.angle(V[2]) - np.angle(V[1]) - np.angle(Y[2, 1])))
    q2_calculated = (abs(V[2]) * abs(V[0]) * abs(Y[2, 0]) * np.sin(np.angle(V[2]) - np.angle(V[0]) - np.angle(Y[2, 0]))
                     + abs(V[2]) * abs(V[1]) * abs(Y[2, 1]) * np.sin(np.angle(V[2]) - np.angle(V[1]) - np.angle(Y[2, 1])))

    f = np.array([p1_calculated, q1_calculated])

    print(f"\nPower Injections of PV and PQ buses for iteration {iteration} (vector f):")
    print(f"Bus {1}: P={f[0]:.4f} Q = {f[1]:.4f}")

    delta_y = y - f

    print(f"\nPower mismatches for iteration{iteration} (vector f):")
    print(f"Bus {1}: P = {delta_y[0]:.4f} Q = {delta_y[1]:.4f}")

    if np.all(np.abs(delta_y) < tolerance):
        print(f"Converged after {iteration + 1} iterations\n")

        print(f"\nFinal Voltage magnitudes and angles:")

        for i in range(3):
            print(f"Bus {i}: V = {abs(V[i]):.4f} p.u. delta = {np.degrees(np.angle(V[i])):.2f} degrees")

        print(f"\nFinal power injections")
        print(f"Bus {0}: P = {p0_calculated:.4f} Q = {q0_calculated:.4f}")
        print(f"Bus {1}: P = {p1_calculated:.4f} Q = {q1_calculated:.4f}")
        print(f"Bus {2}: P = {p2_calculated:.4f} Q = {q2_calculated:.4f}")

        break

    J1 = -abs(V[1]) * (abs(Y[1, 0]) * abs(V[0]) * np.sin(np.angle(V[1]) - np.angle(V[0]) - np.angle(Y[1, 0])))

    J2 = (abs(V[1]) * abs(Y[1, 1]) * np.cos(np.angle(Y[1, 1]))
          + abs(Y[1, 0]) * abs(V[0]) * np.cos(np.angle(V[1]) - np.angle(V[0]) - np.angle(Y[1, 0]))
          + abs(Y[1, 1]) * abs(V[1]) * np.cos(np.angle(V[1]) - np.angle(V[1]) - np.angle(Y[1, 1])))

    J3 = abs(V[1]) * (abs(Y[1, 0]) * abs(V[0]) * np.cos(np.angle(V[1]) - np.angle(V[0]) - np.angle(Y[1, 0])))

    J4 = (-abs(V[1]) * abs(Y[1, 1]) * np.sin(np.angle(Y[1, 1]))
          + abs(Y[1, 0]) * abs(V[0]) * np.sin(np.angle(V[1]) - np.angle(V[0]) - np.angle(Y[1, 0]))
          + abs(Y[1, 1]) * abs(V[1]) * np.sin(np.angle(V[1]) - np.angle(V[1]) - np.angle(Y[1, 1])))

    J5 = -abs(V[2]) * abs(Y[2, 0]) * abs(V[0]) * np.cos(np.angle(V[2]) - np.angle(V[0]) - np.angle(Y[2, 0]))

    J6 = abs(Y[2, 1]) * abs(V[2]) * np.sin(np.angle(V[2]) - np.angle(V[1]) - np.angle(Y[2, 1])) - abs(V[2]) * abs(
        Y[2, 0]) * abs(V[0]) * np.sin(np.angle(V[2]) - np.angle(V[0]) - np.angle(Y[2, 0]))

    J7 = -abs(Y[2, 1]) * abs(V[2]) * np.cos(np.angle(V[2]) - np.angle(V[1]) - np.angle(Y[2, 1])) + abs(V[2]) * abs(
        Y[2, 0]) * abs(V[0]) * np.cos(np.angle(V[2]) - np.angle(V[0]) - np.angle(Y[2, 0]))

    J8 = abs(Y[2, 1]) * abs(V[2]) * np.sin(np.angle(V[2]) - np.angle(V[1]) - np.angle(Y[2, 1])) + abs(V[2]) * abs(
        Y[2, 0]) * abs(V[1]) * np.sin(np.angle(V[2]) - np.angle(V[1]) - np.angle(Y[2, 0]))

    J9 = abs(Y[2, 1]) * abs(V[2]) * np.cos(np.angle(V[2]) - np.angle(V[1]) - np.angle(Y[2, 1])) - abs(V[2]) * abs(
        Y[2, 0]) * abs(V[1]) * np.cos(np.angle(V[2]) - np.angle(V[1]) - np.angle(Y[2, 0]))

    J = np.array([[J1, J2, J3],
              [J4, J5, J6],
              [J7, J8, J9]])

    delta_x = np.linalg.solve(J, delta_y)
    x += delta_x

    V = np.array([v0 * np.exp(1j * ang0), x[1] * np.exp(1j * x[0]), x[3] * np.exp(1j * x[2])])

    print(f"\nVoltage magnitudes and angles for iteration {iteration}:")

   # for i in range(3):
      #  print(f"Bus {i}: V = {abs(V[i]):.4f} p.u delta = {np.degrees(np.angle(V[i])):.2f} degrees")