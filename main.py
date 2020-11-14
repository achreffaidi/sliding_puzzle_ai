from Solver import Solver
import random

from solvers.taquin_solver_advanced import SlidingPuzzleAdvanced
from solvers.taquin_solver_simple import SlidingPuzzleSimple


def generate_random_positions() -> []:
    initial_random_values = []
    for x in range(3):
        for y in range(3):
            initial_random_values.append((x, y))
    random.shuffle(initial_random_values)
    return initial_random_values


random_values = generate_random_positions()
solver_simple = Solver(SlidingPuzzleSimple(random_values))
solver_advanced = Solver(SlidingPuzzleAdvanced(random_values))
print(random_values)
solver_simple.solve(False)
solver_advanced.solve(False)
