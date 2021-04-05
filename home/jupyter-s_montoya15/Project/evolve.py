def evolve(lamb = 1, dt = 0.0001, N0 = 1000, T = 10):
    t = 0
    times = [t]
    current_N = [N0]

    while t <= T:
        N = N0 - lamb * N0 * dt
        t = t + dt
        times.append(t)
        current_N.append(N)
        N0 = N
    return (times, current_N)