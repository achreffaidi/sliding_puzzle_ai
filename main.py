from Solver import Solver
import random

from solvers.Benchmarking.simulator import Simulator
from solvers.taquin_solver_advanced import SlidingPuzzleAdvanced
from solvers.taquin_solver_simple import SlidingPuzzleSimple


def generate_random_positions(n) -> []:
    initial_random_values = []
    for x in range(n):
        for y in range(n):
            initial_random_values.append((x, y))
    random.shuffle(initial_random_values)
    return [(1, 0), (0, 1), (0, 2),
            (1, 2), (0, 0), (2, 2),
            (1, 1), (2, 0), (2, 1)]

    return initial_random_values


s = Simulator([(4, 4)], [20])
s.simulate()
