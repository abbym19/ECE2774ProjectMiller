import numpy as np

z01 = 1j * 0.05

Y = np.array([[1 / z01, -1 / z01],
              [-1 / z01, 1 / z01]])

v0 = 1.0
ang0 = 0.0

p1 = -1
q1 = -0.2
v1 = 1.0
ang1 = 0

V = np.array([v0 * np.exp(1j * ang0), v1 * np.exp(1j * ang1)])

p1_inj = p1
q1_inj = q1

y = np.array([p1_inj, q1_inj])
print("Power injections of PV and PQ buses:\n")
print(f"Bus {1}: P = {y[0]:.4f} Q = {y[1]:.4f}")

x = np.array([ang1, abs(v1)])

max_iterations = 100
tolerance = 1e-8

for iteration in range(max_iterations):

    print(f"\n\n--------Iteration {iteration}---------")

    p0_calculated = (abs(V[0]) * abs(V[0]) * abs(Y[0, 0]) * np.cos(np.angle(V[0]) - np.angle(V[0]) - np.angle(Y[0, 0])
    + abs(V[0]) * abs(V[1]) * abs(Y[0, 1]) * np.cos(np.angle(V[0])) - np.angle(V[1]) - np.angle(Y[0, 1])))

    p1_calculated = (abs(V[1]) * abs(V[0]) * abs(Y[1, 0]) * np.cos(np.angle(V[1]) - np.angle(V[0]) - np.angle(Y[1, 0])
    + abs(V[1]) * abs(V[1]) * abs(Y[1, 1]) * np.cos(np.angle(V[1])) - np.angle(V[1]) - np.angle(Y[1, 1])))

    q0_calculated = (abs(V[0]) * abs(V[0]) * abs(Y[0, 0]) * np.sin(np.angle(V[0]) - np.angle(V[0]) - np.angle(Y[0, 0])
    + abs(V[0]) * abs(V[1]) * abs(Y[0, 1]) * np.sin(np.angle(V[0])) - np.angle(V[1]) - np.angle(Y[0, 1])))

    q1_calculated = (abs(V[1]) * abs(V[0]) * abs(Y[1, 0]) * np.sin(np.angle(V[1]) - np.angle(V[0]) - np.angle(Y[1, 0])
    + abs(V[1]) * abs(V[1]) * abs(Y[1, 1]) * np.sin(np.angle(V[1])) - np.angle(V[1]) - np.angle(Y[1, 1])))

    f = np.array([p1_calculated, q1_calculated])

    print(f"\nPower Injections of PV and PQ buses for iteration {iteration} (vector f):")
    print(f"Bus {1}: P={f[0]:.4f} Q = {f[1]:.4f}")

    delta_y = y-f

    print(f"\nPower mismatches for iteration{iteration} (vector f):")
    print(f"Bus {1}: P = {delta_y[0]:.4f} Q = {delta_y[1]:.4f}")

    if np.all(np.abs(delta_y) < tolerance):
        print(f"Converged after {iteration+1} iterations\n")

        print(f"\nFinal Voltage magnitudes and angles:")

        for i in range(2):
            print(f"Bus {i}: V = {abs(V[i]):.4f} p.u. delta = {np.degrees(np.angle(V[i])):.2f} degrees")

        print(f"\nFinal power injections")
        print(f"Bus {0}: P = {p0_calculated:.4f} Q = {q0_calculated:.4f}")
        print(f"Bus {1}: P = {p1_calculated:.4f} Q = {q1_calculated:.4f}")

        break

    J1 = -abs(V[1]) * (abs(Y[1,0]) * abs(V[0]) * np.sin(np.angle(V[1]) - np.angle(V[0]) - np.angle(Y[1,0])))

    J2 = (abs(V[1]) * abs(Y[1,1]) *  np.cos(np.angle(Y[1,1]))
            + abs(Y[1,0]) * abs(V[0]) * np.cos(np.angle(V[1]) - np.angle(V[0]) - np.angle(Y[1,0]))
            + abs(Y[1, 1]) * abs(V[1]) * np.cos(np.angle(V[1]) - np.angle(V[1]) - np.angle(Y[1, 1])))

    J3 = abs(V[1]) * (abs(Y[1,0]) * abs(V[0]) * np.cos(np.angle(V[1]) - np.angle(V[0]) - np.angle(Y[1,0])))

    J4 = (-abs(V[1]) * abs(Y[1,1]) *  np.sin(np.angle(Y[1,1]))
            + abs(Y[1,0]) * abs(V[0]) * np.sin(np.angle(V[1]) - np.angle(V[0]) - np.angle(Y[1,0]))
            + abs(Y[1, 1]) * abs(V[1]) * np.sin(np.angle(V[1]) - np.angle(V[1]) - np.angle(Y[1, 1])))

    J = np.array([[J1, J2], [J3, J4]])

    delta_x = np.linalg.solve(J, delta_y)
    x += delta_x

    V = np.array([v0 * np.exp(1j * ang0), x[1] * np.exp(1j * x[0])])

    print(f"\nVoltage magnitudes and angles for iteration {iteration}:")

    for i in range (2):
        print(f"bus {i}: V = {abs(V[i]):.4f} p.u delta = {np.degrees(np.angle(V[i])):.2f} degrees")




