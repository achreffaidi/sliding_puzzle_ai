import random

from Solver import Solver
from solvers.Benchmarking.random_puzzle_generator import generate_random_board
from solvers.taquin_solver_advanced import SlidingPuzzleAdvanced
from solvers.taquin_solver_simple import SlidingPuzzleSimple


class Simulator:
    def __init__(self, sizes, number_of_moves) -> None:
        self.sizes = sizes
        self.number_of_moves = number_of_moves
        super().__init__()

    def simulate(self):
        output = []
        for size in self.sizes:
            (m, n) = size
            for moves in self.number_of_moves:
                random_values = generate_random_board(m, n, moves)
                solver_simple = Solver(SlidingPuzzleSimple(random_values, m, n))
                solver_advanced = Solver(SlidingPuzzleAdvanced(random_values, m, n))
                solver_advanced.solve(True)
                solver_simple.solve(False)
                output.append({
                    'size': (m, n),
                    'number of moves': moves,
                    'basic H': solver_simple.iterations,
                    'advanced H': solver_advanced.iterations
                })
        print(output)
