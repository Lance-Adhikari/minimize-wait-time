# Sample appointment durations.
patients = [15, 20, 10]


def min_total_waiting_time(patients):
    # Serve shorter appointments first to minimize total waiting time.
    times = sorted(patients)

    waiting_time = 0
    n = len(patients)

    for i in range(n):
        # This appointment adds to the wait of every patient after it.
        waiting_time = waiting_time + (n - i - 1) * times[i]

    return waiting_time


print(min_total_waiting_time(patients))
