import matplotlib.pyplot as plt

def plot_closest_pair(points, result):
    closest_pair = (result[1], result[2])
    x = [p[0] for p in points]
    y = [p[1] for p in points]

    plt.scatter(x, y)

    p1, p2 = closest_pair

    plt.plot(
        [p1[0], p2[0]],
        [p1[1], p2[1]]
    )

    plt.show()

import time
import matplotlib.pyplot as plt

from src.closest_pair.brute_force import run as run_brute_force
from src.closest_pair.divide_and_conquer import run as run_divide_and_conquer
from src.geometry.utils import random_points2D


def performance_test(sizes, repetitions=5):
    brute_times = []
    divide_times = []

    for n in sizes:
        brute_total = 0
        divide_total = 0

        for _ in range(repetitions):
            points = random_points2D(n)

            start = time.perf_counter()
            run_brute_force(points)
            brute_total += time.perf_counter() - start

            start = time.perf_counter()
            run_divide_and_conquer(points)
            divide_total += time.perf_counter() - start

        brute_times.append(brute_total / repetitions)
        divide_times.append(divide_total / repetitions)

        print(
            f"n={n:6d} | "
            f"Brute: {brute_times[-1]:.6f}s | "
            f"Divide: {divide_times[-1]:.6f}s"
        )

    return brute_times, divide_times


sizes = [100, 200, 500, 1000, 2000, 5000]

brute_times, divide_times = performance_test(sizes, repetitions=10)

plt.plot(sizes, brute_times, marker="o", label="Brute Force")
plt.plot(sizes, divide_times, marker="o", label="Divide and Conquer")

plt.xlabel("Número de pontos")
plt.ylabel("Tempo médio (s)")
plt.title("Closest Pair - Comparação de Performance")
plt.legend()
plt.grid()

plt.show()