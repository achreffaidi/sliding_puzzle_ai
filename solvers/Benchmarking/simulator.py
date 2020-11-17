import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import style
import numpy as np

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
                solver_advanced.solve(False)
                solver_simple.solve(False)
                output.append({
                    'size': (m, n),
                    'number_moves': moves,
                    'basicH': solver_simple.iterations,
                    'advancedH': solver_advanced.iterations
                })
        x1 = []
        x2 = []
        y1 = []
        y2 = []

        for value in output:
            (m, n) = value['size']
            x1.append(value['number_moves'])
            x2.append(m * n)
            y1.append(value['basicH'])
            y2.append(value['advancedH'])
        if len(self.number_of_moves) > 1 and len(self.sizes) > 1 :
            fig = plt.figure(1)
            ax = fig.add_subplot(111, projection='3d')
            ax.plot_trisurf(x1, x2, y1, color='red', edgecolors='black', alpha=0.8)
            ax.plot_trisurf(x1, x2, y2, color='blue', edgecolors='black', alpha=0.8)

        else:
            if len(self.number_of_moves) > 1:
                f1 = plt.figure(1)
                plt.plot(x1, y1, label='Basic Algo')
                plt.plot(x1, y2, label='Advanced Algo')
                plt.xlabel('number of changes')
                plt.ylabel('number of iterations')
                plt.title('How difficulty affects both algo ')
                plt.legend()
            if len(self.sizes) > 1:
                f2 = plt.figure(2)
                plt.plot(x2, y1, label='Basic Algo')
                plt.plot(x2, y2, label='Advanced Algo')
                plt.xlabel('Input size : m x n ')
                plt.ylabel('number of iterations')
                plt.title('how  input size affects both algo ')
                plt.legend()

        plt.show()
