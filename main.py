from Solver import Solver
import random

from solvers.Benchmarking.simulator import Simulator
from solvers.taquin_solver_advanced import SlidingPuzzleAdvanced
from solvers.taquin_solver_simple import SlidingPuzzleSimple


s = Simulator([(3, 3),(4, 4)], [2,3,4,5,6,7,8,9,10])
s.simulate()
